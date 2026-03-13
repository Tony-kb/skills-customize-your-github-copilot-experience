"""Starter code for the Python Data Visualization assignment.

You may use matplotlib or plotly to complete this assignment.
"""

import csv


def load_data(file_path):
    """Load CSV data and return rows as a list of dictionaries."""
    rows = []
    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            rows.append(row)
    return rows


def clean_data(rows):
    """Convert numeric fields and skip rows with missing values."""
    cleaned = []
    for row in rows:
        if not row["month"] or not row["sales"] or not row["region"]:
            continue
        try:
            row["sales"] = float(row["sales"])
        except ValueError:
            continue
        cleaned.append(row)
    return cleaned


def create_line_chart(data):
    """TODO: Create a line chart using matplotlib or plotly."""
    # Suggested output file name: monthly_sales_trend.png
    raise NotImplementedError("Implement create_line_chart")


def create_bar_chart(data):
    """TODO: Create a bar chart by region using matplotlib or plotly."""
    # Suggested output file name: region_comparison.png
    raise NotImplementedError("Implement create_bar_chart")


def write_insights(data, output_path="insights.txt"):
    """TODO: Write 3-5 sentences describing patterns in the charts."""
    raise NotImplementedError("Implement write_insights")


def main():
    input_file = "sample-data.csv"
    rows = load_data(input_file)
    cleaned = clean_data(rows)

    print(f"Loaded {input_file}")
    print(f"Rows loaded: {len(cleaned)}")

    create_line_chart(cleaned)
    create_bar_chart(cleaned)
    write_insights(cleaned)

    print("Created line chart: monthly_sales_trend.png")
    print("Created bar chart: region_comparison.png")
    print("Insight summary saved to insights.txt")


if __name__ == "__main__":
    main()
