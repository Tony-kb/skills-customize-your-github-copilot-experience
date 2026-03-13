# 📘 Assignment: Python Text Processing

## 🎯 Objective

Practice text processing in Python by reading from files, cleaning and analyzing text, and writing results to an output file. By the end of this assignment, you will build reusable functions for common string and file I/O workflows.

## 📝 Tasks

### 🛠️ Load and Normalize Text Data

#### Description
Write code to open a text file, read its contents, and normalize the text so it is easier to analyze.

#### Requirements
Completed program should:

- Read text from `sample-input.txt` using file I/O.
- Convert all text to lowercase.
- Remove common punctuation marks (`. , ! ? : ;`).
- Return the cleaned text as a string.


### 🛠️ Analyze Word Usage

#### Description
Create functions that split cleaned text into words and compute basic statistics.

#### Requirements
Completed program should:

- Count the total number of words.
- Count the number of unique words.
- Build a frequency dictionary where each word maps to its count.
- Print the top 5 most frequent words in descending order.


### 🛠️ Save a Text Analysis Report

#### Description
Generate a summary report of your analysis and save it to a file.

#### Requirements
Completed program should:

- Create a report containing total words, unique words, and top 5 words.
- Write the report to `analysis-report.txt`.
- Display a confirmation message after saving the file.
- Include one example run in a code block showing expected input/output behavior.

Example run:

```text
Loaded sample-input.txt
Total words: 42
Unique words: 25
Top 5 words: python(6), data(4), text(3), file(3), processing(2)
Report saved to analysis-report.txt
```
