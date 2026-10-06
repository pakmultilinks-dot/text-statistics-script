"""Text Statistics Script - analyzes a piece of text.

Usage:
    python text_stats.py <file.txt>     # analyze a text file
    python text_stats.py                 # paste/type text, then Ctrl+D (Ctrl+Z on Windows)

Prints: word count, sentence count, and the 5 most common words.
"""

import re
import sys
from collections import Counter


def split_sentences(text):
    """Split text into sentences on . ! ? followed by whitespace or end."""
    parts = re.split(r'[.!?]+(?:\s+|$)', text.strip())
    return [p for p in parts if p.strip()]


def tokenize(text):
    """Return lowercase word tokens (letters, digits, apostrophes)."""
    return re.findall(r"[a-z0-9']+", text.lower())


def analyze(text):
    """Return dict with word_count, sentence_count, top_words (list of 5 tuples)."""
    words = tokenize(text)
    sentences = split_sentences(text)
    counts = Counter(words)
    top = counts.most_common(5)
    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "top_words": top,
    }


def report(stats):
    """Print a human-readable report."""
    print(f"Word count: {stats['word_count']}")
    print(f"Sentence count: {stats['sentence_count']}")
    print("Top 5 most common words:")
    if not stats["top_words"]:
        print("  (no words found)")
    for word, count in stats["top_words"]:
        print(f"  {word}: {count}")


def read_input():
    """Read from a file argument or from stdin (pasted text)."""
    if len(sys.argv) > 1:
        path = sys.argv[1]
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    print("Paste your text below, then press Ctrl+D (Linux/Mac) or Ctrl+Z then Enter (Windows):")
    return sys.stdin.read()


def main():
    text = read_input()
    if not text.strip():
        print("No text provided.")
        sys.exit(1)
    report(analyze(text))


if __name__ == "__main__":
    main()
