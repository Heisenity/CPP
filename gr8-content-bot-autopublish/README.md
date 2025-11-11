# gr8-content-bot-autopublish

`gr8-content-bot-autopublish` is a fully autonomous WordPress blog content upgrader designed to automatically improve and republish existing blog posts. The system is built to enhance content to meet AdSense quality standards by improving helpfulness, formatting, and clarity, while also adding valuable sections such as examples, step-by-step guides, comparison tables, and FAQs. It is equipped with content safety guards to ensure all published material is compliant with AdSense policies.

## Features

- **Automated Content Upgrades**: Fetches all published posts from a WordPress site and identifies those that require improvement based on word count, heading structure, and content repetition.
- **Advanced Rewriting**: Utilizes a powerful LLM to rewrite and enhance blog posts, adding valuable sections and removing generic filler content.
- **Content Safety Guards**: Before publishing, the system checks for forbidden keywords, minimum word count, and repeated sentences to ensure AdSense compliance.
- **Backup and Restore**: Automatically backs up the original content both locally and on the WordPress server before making any changes. A `rollback` command is available to restore the original content if needed.
- **Idempotency**: Maintains a state file to track upgraded posts, preventing the same post from being processed multiple times unless explicitly forced.
- **CLI Interface**: A user-friendly command-line interface allows for easy management of the content upgrade process, with commands to `scan`, `upgrade`, `rollback`, and check the `status`.
- **GitHub Actions Automation**: Includes a pre-configured GitHub Actions workflow to run the content upgrade process on a nightly basis, ensuring your blog is continuously improved without manual intervention.

## Getting Started

### Prerequisites

- Python 3.11 or higher
- A WordPress site with the REST API enabled
- An Application Password for your WordPress user
- An API key for the LLM you intend to use

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/gr8-content-bot-autopublish.git
   cd gr8-content-bot-autopublish
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your environment variables:**
   - Copy the `.env.example` file to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Open the `.env` file and add your WordPress and LLM credentials.

### Usage

The `gr8-content-bot-autopublish` tool is managed through a simple command-line interface. Below are the available commands and their usage.

- **scan**: Scans all published posts and identifies those that need improvement.
  ```bash
  python gr8_content_bot/main.py scan
  ```

- **upgrade**: Rewrites and publishes a limited number of posts.
  ```bash
  python gr8_content_bot/main.py upgrade --limit 5
  ```
  - Use the `--force` flag to reprocess posts that have already been upgraded.

- **rollback**: Restores a post to its original content from a backup.
  ```bash
  python gr8_content_bot/main.py rollback --post-id 123
  ```

- **status**: Shows the current progress of the content upgrade.
  ```bash
  python gr8_content_bot/main.py status
  ```

## Automation with GitHub Actions

The repository includes a GitHub Actions workflow defined in `.github/workflows/autopublish.yml`. This workflow is configured to run on a nightly basis and will automatically upgrade a predefined number of posts. To enable this automation, you will need to add the following secrets to your GitHub repository:

- `WP_BASE_URL`
- `WP_USER`
- `WP_APP_PASSWORD`
- `LLM_API_KEY`
- `MODEL_NAME`

Once these secrets are configured, the workflow will run as scheduled, keeping your content fresh and high-quality without any manual effort.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
