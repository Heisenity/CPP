import json
import os
from dotenv import load_dotenv

from gr8_content_bot.wordpress_client import WordPressClient
from gr8_content_bot.post_auditor import PostAuditor
from gr8_content_bot.rewriter import Rewriter
from gr8_content_bot.safety_guards import SafetyGuards

class Pipeline:
    """Orchestrates the entire content upgrade workflow."""

    def __init__(self, force_upgrade=False):
        """Initializes the pipeline."""
        load_dotenv()
        self.state_file = "state.json"
        self.state = self._load_state()
        self.force_upgrade = force_upgrade
        self.dry_run = os.getenv('DRY_RUN', 'false').lower() == 'true'

        self.wp_client = WordPressClient(
            base_url=os.getenv('WP_BASE_URL'),
            user=os.getenv('WP_USER'),
            app_password=os.getenv('WP_APP_PASSWORD')
        )
        self.auditor = PostAuditor()
        self.rewriter = Rewriter(
            api_key=os.getenv('LLM_API_KEY'),
            model_name=os.getenv('MODEL_NAME')
        )
        self.safety_guards = SafetyGuards()

    def _load_state(self):
        """Loads the state from the state file."""
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                return json.load(f)
        return {}

    def _save_state(self):
        """Saves the current state to the state file."""
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=4)

    def scan(self):
        """Scans all posts and identifies those needing improvement."""
        print("Scanning all published posts...")
        posts = self.wp_client.get_all_posts()
        needs_improvement_list = []

        for post in posts:
            post_id = post['id']
            content = post.get('content', {}).get('rendered', '')
            needs_fix, reason = self.auditor.needs_improvement(content)

            if needs_fix:
                print(f"Post ID {post_id} needs improvement: {reason}")
                needs_improvement_list.append(post)

        print(f"\nFound {len(needs_improvement_list)} posts that need improvement.")
        return needs_improvement_list

    def upgrade(self, limit=5):
        """Upgrades a limited number of posts."""
        print(f"Starting upgrade process with a limit of {limit} posts...")
        posts_to_fix = self.scan()
        upgraded_count = 0

        for post in posts_to_fix:
            if upgraded_count >= limit:
                break

            post_id = post['id']
            if str(post_id) in self.state and not self.force_upgrade:
                print(f"Skipping post {post_id} as it has already been upgraded.")
                continue

            print(f"\n--- Upgrading Post ID: {post_id} ---")
            title = post.get('title', {}).get('rendered', '')
            original_content = post.get('content', {}).get('rendered', '')

            # 1. Backup the post
            if not self.dry_run:
                self.wp_client.backup_post(post_id, original_content)
            else:
                print(f"[DRY RUN] Would have backed up post {post_id}.")

            # 2. Rewrite the content
            print("Rewriting content with LLM...")
            rewritten_content = self.rewriter.rewrite(title, original_content)
            if not rewritten_content or rewritten_content == "[[SKIP_UNSAFE]]":
                print(f"Skipping post {post_id} due to unsafe content or rewrite error.")
                continue

            # 3. Perform safety checks
            is_safe, reason = self.safety_guards.is_safe(rewritten_content)
            if not is_safe:
                print(f"Skipping post {post_id} due to safety guard failure: {reason}")
                continue

            # 4. Publish the new content
            if not self.dry_run:
                print(f"Publishing upgraded content for post {post_id}...")
                self.wp_client.update_post(post_id, rewritten_content)
                self.state[str(post_id)] = {'status': 'upgraded', 'last_updated': post['modified']}
                self._save_state()
            else:
                print(f"[DRY RUN] Would have published rewritten content for post {post_id}.")

            upgraded_count += 1
            print(f"--- Finished Post ID: {post_id} ---")

        print(f"\nUpgrade process completed. {upgraded_count} posts upgraded.")

    def rollback(self, post_id):
        """Rolls back a post to its original content."""
        print(f"Rolling back post {post_id} to its original content...")
        if self.dry_run:
            print(f"[DRY RUN] Would have rolled back post {post_id}.")
            return

        restored_post = self.wp_client.rollback_post(post_id)
        if restored_post:
            print(f"Post {post_id} has been successfully restored.")
            if str(post_id) in self.state:
                del self.state[str(post_id)]
                self._save_state()
        else:
            print(f"Failed to roll back post {post_id}.")

    def status(self):
        """Shows the progress of the content upgrade."""
        total_posts = len(self.wp_client.get_all_posts())
        upgraded_posts = len(self.state)

        if total_posts > 0:
            percentage = (upgraded_posts / total_posts) * 100
            print(f"Total Posts: {total_posts}")
            print(f"Upgraded Posts: {upgraded_posts}")
            print(f"Progress: {percentage:.2f}%")
        else:
            print("Could not fetch total number of posts.")
