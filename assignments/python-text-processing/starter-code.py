"""Starter code for the Python Text Processing assignment."""


def load_and_normalize_text(file_path):
    """Read text from a file and return a cleaned, lowercase string."""
    # TODO: Implement file reading and text normalization.
    # - Read file contents
    # - Convert to lowercase
    # - Remove punctuation: . , ! ? : ;
    raise NotImplementedError("Implement load_and_normalize_text")


def build_word_frequency(cleaned_text):
    """Return a dictionary mapping words to their frequency counts."""
    # TODO: Split text into words and count frequency.
    raise NotImplementedError("Implement build_word_frequency")


def get_top_words(word_frequency, limit=5):
    """Return a list of (word, count) tuples for the most frequent words."""
    # TODO: Sort by descending count, then alphabetically for ties.
    raise NotImplementedError("Implement get_top_words")


def write_report(output_path, total_words, unique_words, top_words):
    """Write analysis results to a report file."""
    # TODO: Write a readable report to output_path.
    raise NotImplementedError("Implement write_report")


def main():
    input_path = "sample-input.txt"
    output_path = "analysis-report.txt"

    cleaned_text = load_and_normalize_text(input_path)
    words = cleaned_text.split()
    word_frequency = build_word_frequency(cleaned_text)
    top_words = get_top_words(word_frequency, limit=5)

    total_words = len(words)
    unique_words = len(word_frequency)

    print(f"Loaded {input_path}")
    print(f"Total words: {total_words}")
    print(f"Unique words: {unique_words}")
    print("Top 5 words:", top_words)

    write_report(output_path, total_words, unique_words, top_words)
    print(f"Report saved to {output_path}")


if __name__ == "__main__":
    main()
