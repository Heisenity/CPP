import re
from collections import Counter
from bs4 import BeautifulSoup

class SafetyGuards:
    """Performs content safety checks to ensure compliance with AdSense policies."""

    def __init__(self, min_word_count=800, min_repeated_words=10):
        """Initializes the safety guards."""
        self.min_word_count = min_word_count
        self.min_repeated_words = min_repeated_words
        self.forbidden_substrings = [
            'porn', 'adult', 'explicit', 'escort', 'gambling', 'betting', 'casino',
            'hacking', 'crack', 'warez', 'illegal download', 'drugs', 'weapons',
            'pharma', 'medical diagnosis', 'financial advice'
        ]

    def is_safe(self, html_content):
        """
        Runs all safety checks on the rewritten content.
        Returns a tuple (is_safe, reason).
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        text = soup.get_text()

        # 1. Check for forbidden substrings
        contains_forbidden, keyword = self._contains_forbidden_substrings(text)
        if contains_forbidden:
            return False, f"Content contains forbidden keyword: {keyword}"

        # 2. Check for minimum word count
        word_count = self._get_word_count(text)
        if word_count < self.min_word_count:
            return False, f"Final word count is {word_count} (less than {self.min_word_count})"

        # 3. Check for repeated sentences
        if self._has_repeated_sentences(text):
            return False, "Rewritten content contains repeated sentences"

        return True, "Content passed all safety checks."

    def _contains_forbidden_substrings(self, text):
        """Checks for forbidden substrings, case-insensitive."""
        lower_text = text.lower()
        for keyword in self.forbidden_substrings:
            if keyword in lower_text:
                return True, keyword
        return False, None

    def _get_word_count(self, text):
        """Calculates the word count."""
        words = re.findall(r'\w+', text)
        return len(words)

    def _has_repeated_sentences(self, text):
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

        return any(count > 1 for count in sentence_counts.values())
