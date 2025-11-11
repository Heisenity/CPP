import re
from collections import Counter
from bs4 import BeautifulSoup

class PostAuditor:
    """Audits a blog post to determine if it needs improvement."""

    def __init__(self, min_word_count=800, min_headings=3, min_repeated_words=10):
        """Initializes the post auditor."""
        self.min_word_count = min_word_count
        self.min_headings = min_headings
        self.min_repeated_words = min_repeated_words

    def needs_improvement(self, post_content):
        """
        Checks if a post needs improvement based on word count, headings, and repeated sentences.
        """
        soup = BeautifulSoup(post_content, 'html.parser')
        text = soup.get_text()

        word_count = self._get_word_count(text)
        heading_count = self._get_heading_count(soup)
        repeated_sentences = self._detect_repeated_sentences(text)

        if word_count < self.min_word_count:
            return True, f"Word count is {word_count} (less than {self.min_word_count})"

        if heading_count < self.min_headings:
            return True, f"Heading count is {heading_count} (less than {self.min_headings})"

        if repeated_sentences:
            return True, f"Found repeated sentences: {', '.join(repeated_sentences)}"

        return False, "Post meets quality standards."

    def _get_word_count(self, text):
        """Calculates the word count of the given text."""
        words = re.findall(r'\w+', text)
        return len(words)

    def _get_heading_count(self, soup):
        """Counts the number of H2 and H3 headings in the HTML."""
        return len(soup.find_all(['h2', 'h3']))

    def _detect_repeated_sentences(self, text):
        """Detects repeated sentences with a minimum word count."""
        sentences = re.split(r'[.!?]', text)

        normalized_sentences = [
            ' '.join(re.findall(r'\w+', s.lower()))
            for s in sentences
        ]

        long_sentences = [
            s for s in normalized_sentences if len(s.split()) >= self.min_repeated_words
        ]

        sentence_counts = Counter(long_sentences)

        repeated = {sentence for sentence, count in sentence_counts.items() if count > 1}

        return list(repeated)

    def audit(self, post):
        """Provides a full audit of a post."""
        post_id = post.get('id', 'N/A')
        post_title = post.get('title', {}).get('rendered', 'N/A')
        post_content = post.get('content', {}).get('rendered', '')

        soup = BeautifulSoup(post_content, 'html.parser')
        text = soup.get_text()

        word_count = self._get_word_count(text)
        heading_count = self._get_heading_count(soup)
        repeated_sentences = self._detect_repeated_sentences(text)

        return {
            "post_id": post_id,
            "title": post_title,
            "word_count": word_count,
            "heading_count": heading_count,
            "repeated_sentences": len(repeated_sentences),
            "details": repeated_sentences
        }
