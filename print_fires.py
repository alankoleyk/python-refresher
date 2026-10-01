import argparse
import statistics
from my_utils import get_column
import os
import sys


# Command-line tool to look up fire/emission data for a given country.
def main():
    parser = argparse.ArgumentParser(
        description="Get a column value for a given country from a CSV file."
    )
    parser.add_argument(
        "country",
        type=str,
        help="Name of the country to look up (e.g. 'United States of America')"
    )
    parser.add_argument(
        "country_column",
        type=int,
        help="Index of the column containing country names"
    )
    parser.add_argument(
        "fires_column",
        type=int,
        help="Index of the column containing fire/emission data to retrieve"
    )
    parser.add_argument(
        "file_name",
        type=str,
        help="Path to the CSV file"
    )
    parser.add_argument(
        "--operation",
        type=str,
        choices=["mean", "median", "std"],
        help="Optional statistical operation to apply to the returned values "
             "(mean, median, or std). If omitted, prints the raw values."
    )

    args = parser.parse_args()

    if not os.path.isfile(args.file_name):
        print(f"Error: file '{args.file_name}' not found.", file=sys.stderr)
        sys.exit(1)

    fires = get_column(
        args.file_name,
        args.country_column,
        args.country,
        result_column=args.fires_column
    )

    if args.operation is None:
        print(fires)
    elif args.operation == "mean":
        print(statistics.mean(fires))
    elif args.operation == "median":
        print(statistics.median(fires))
    elif args.operation == "std":
        print(statistics.stdev(fires))


if __name__ == "__main__":
    main()
