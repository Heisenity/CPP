import argparse
import os
from dotenv import load_dotenv

from gr8_content_bot.pipeline import Pipeline

def main():
    """Main function to run the gr8-content-bot CLI."""
    load_dotenv()

    parser = argparse.ArgumentParser(description="A bot to automatically upgrade WordPress blog content.")
    subparsers = parser.add_subparsers(dest="command", required=True, help="Available commands")

    # 'scan' command
    parser_scan = subparsers.add_parser("scan", help="Scan all posts and identify those needing improvement.")

    # 'upgrade' command
    parser_upgrade = subparsers.add_parser("upgrade", help="Rewrite and publish N posts at a time.")
    parser_upgrade.add_argument("--limit", type=int, default=int(os.getenv('MAX_POSTS_PER_RUN', 5)),
                                help="The maximum number of posts to upgrade in one run.")
    parser_upgrade.add_argument("--force", action="store_true",
                                help="Force the upgrade of posts that have already been processed.")

    # 'rollback' command
    parser_rollback = subparsers.add_parser("rollback", help="Restore content from a backup.")
    parser_rollback.add_argument("--post-id", type=int, required=True,
                                 help="The ID of the post to roll back.")

    # 'status' command
    parser_status = subparsers.add_parser("status", help="Show the current upgrade progress.")

    args = parser.parse_args()

    pipeline = Pipeline(force_upgrade=getattr(args, 'force', False))

    if args.command == "scan":
        pipeline.scan()
    elif args.command == "upgrade":
        pipeline.upgrade(limit=args.limit)
    elif args.command == "rollback":
        pipeline.rollback(post_id=args.post_id)
    elif args.command == "status":
        pipeline.status()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
