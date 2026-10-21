import sys

from .analysis import average_value1_by_type
from .chart import render_bar_chart
from .io import load_rows


def main():
    csv_path = sys.argv[1]
    rows = load_rows(csv_path)
    averages = average_value1_by_type(rows)
    render_bar_chart(averages)


if __name__ == "__main__":
    main()
