import os
import openai

class Rewriter:
    """Handles the rewriting of blog posts using an LLM."""

    def __init__(self, api_key, model_name, prompt_template_path="prompts/prompt_template.md"):
        """Initializes the rewriter."""
        if not api_key:
            raise ValueError("LLM API key is required.")

        self.api_key = api_key
        self.model_name = model_name
        self.prompt_template = self._load_prompt_template(prompt_template_path)
        self.client = openai.OpenAI(api_key=self.api_key)

    def _load_prompt_template(self, path):
        """Loads the prompt template from a file."""
        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Prompt template not found at {path}")

    def rewrite(self, title, content):
        """Rewrites the post content using the configured LLM."""
        if not self.prompt_template:
            raise ValueError("Prompt template is not loaded.")

        prompt = self.prompt_template.replace("{{TITLE}}", title).replace("{{CONTENT}}", content)

        try:
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are an expert editor improving a WordPress blog post."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4096,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )

            rewritten_content = response.choices[0].message.content.strip()

            if "[[SKIP_UNSAFE]]" in rewritten_content:
                return "[[SKIP_UNSAFE]]"

            return rewritten_content

        except openai.APIError as e:
            print(f"Error during LLM API call: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
