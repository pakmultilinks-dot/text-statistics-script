"""Automated tests for text_stats.py. Run with: python -m pytest test_text_stats.py -v"""

from text_stats import analyze, tokenize, split_sentences


def test_word_count_simple():
    stats = analyze("hello world")
    assert stats["word_count"] == 2


def test_sentence_count():
    stats = analyze("Hello world. How are you? I am fine!")
    assert stats["sentence_count"] == 3


def test_top_words_order():
    stats = analyze("apple banana apple cherry apple banana")
    top = stats["top_words"]
    assert top[0] == ("apple", 3)
    assert top[1] == ("banana", 2)
    assert len(top) == 3  # only 3 unique words


def test_case_insensitive():
    stats = analyze("Hello HELLO hello")
    assert stats["word_count"] == 3
    assert stats["top_words"][0] == ("hello", 3)


def test_top_five_limit():
    text = "one two three four five six seven eight"
    stats = analyze(text)
    assert len(stats["top_words"]) == 5


def test_empty_text():
    stats = analyze("")
    assert stats["word_count"] == 0
    assert stats["sentence_count"] == 0
    assert stats["top_words"] == []


def test_punctuation_ignored():
    stats = analyze("Hello, world! Hello... world?")
    assert stats["word_count"] == 4
    assert stats["top_words"][0][1] == 2  # hello appears twice
