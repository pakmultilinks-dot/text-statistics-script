# Text Statistics Script

A small Python script that analyzes a piece of text and prints word count, sentence count, and the 5 most common words.

## Requirements

- Python 3.8 or newer (no third-party packages needed)

## Usage

Analyze a text file:

```
python text_stats.py sample.txt
```

Or paste text directly (then press Ctrl+D on Linux/Mac, Ctrl+Z then Enter on Windows):

```
python text_stats.py
```

## Example

```
$ python text_stats.py sample.txt
Word count: 42
Sentence count: 5
Top 5 most common words:
  the: 6
  quick: 3
  fox: 2
  brown: 2
  dog: 2
```

## How it works

- **Words** are matched with a regex (`[a-z0-9']+`) after lowercasing, so "Hello" and "hello" count as the same word and punctuation is ignored.
- **Sentences** are split on `.`, `!`, `?` followed by whitespace.
- **Top words** use `collections.Counter.most_common(5)`.

## Tests

7 automated tests in `test_text_stats.py`. Run them with:

```
python -m pytest test_text_stats.py -v
```

Tests cover: word count, sentence count, top-word ordering, case insensitivity, the 5-word limit, empty input, and punctuation handling.
