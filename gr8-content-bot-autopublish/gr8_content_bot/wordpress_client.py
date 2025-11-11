import base64
import json
import os
import requests

class WordPressClient:
    """A client for interacting with the WordPress REST API."""

    def __init__(self, base_url, user, app_password):
        """Initializes the WordPress client."""
        self.base_url = base_url
        self.api_url = f"{self.base_url}/wp-json/wp/v2"

        if not user or not app_password:
            raise ValueError("WordPress user and application password are required.")

        credentials = f"{user}:{app_password}"
        self.token = base64.b64encode(credentials.encode('utf-8'))
        self.headers = {
            'Authorization': f'Basic {self.token.decode("utf-8")}',
            'Content-Type': 'application/json',
            'User-Agent': 'gr8-content-bot/1.0'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def get_all_posts(self):
        """Fetches all published posts from the WordPress site."""
        posts = []
        page = 1
        per_page = 100

        while True:
            params = {
                'per_page': per_page,
                'page': page,
                'status': 'publish',
                '_fields': 'id,slug,title,content,link,date,modified'
            }
            try:
                response = self.session.get(f"{self.api_url}/posts", params=params, timeout=30)
                response.raise_for_status()

                current_posts = response.json()
                if not current_posts:
                    break

                posts.extend(current_posts)
                page += 1

            except requests.exceptions.RequestException as e:
                print(f"Error fetching posts: {e}")
                break

        return posts

    def backup_post(self, post_id, content):
        """Creates a backup of the post content."""
        self.backup_locally(post_id, content)
        self.backup_on_wordpress(post_id, content)

    def backup_locally(self, post_id, content):
        """Saves a local backup of the post content."""
        if not os.path.exists('backups'):
            os.makedirs('backups')

        backup_path = os.path.join('backups', f'{post_id}.html')
        try:
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Local backup for post {post_id} created at {backup_path}")
        except IOError as e:
            print(f"Error creating local backup for post {post_id}: {e}")

    def backup_on_wordpress(self, post_id, content):
        """Saves a backup of the post content to a meta field."""
        payload = {
            'meta': {
                '_gr8_backup_content_v1': content
            }
        }
        try:
            response = self.session.post(f"{self.api_url}/posts/{post_id}", json=payload, timeout=30)
            response.raise_for_status()
            print(f"WordPress meta backup for post {post_id} completed.")
        except requests.exceptions.RequestException as e:
            print(f"Error creating WordPress backup for post {post_id}: {e}")

    def update_post(self, post_id, new_content):
        """Updates a post with new content."""
        payload = {
            'content': new_content,
            'status': 'publish'
        }
        try:
            response = self.session.post(f"{self.api_url}/posts/{post_id}", json=payload, timeout=60)
            response.raise_for_status()
            print(f"Post {post_id} updated successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating post {post_id}: {e}")
            return None

    def rollback_post(self, post_id):
        """Restores a post from a local backup."""
        backup_path = os.path.join('backups', f'{post_id}.html')
        if not os.path.exists(backup_path):
            print(f"No local backup found for post {post_id}.")
            return None

        try:
            with open(backup_path, 'r', encoding='utf-8') as f:
                content_to_restore = f.read()

            print(f"Restoring post {post_id} from {backup_path}...")
            return self.update_post(post_id, content_to_restore)
        except IOError as e:
            print(f"Error reading backup file for post {post_id}: {e}")
            return None
