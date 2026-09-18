import argparse
from my_utils import get_column


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

    args = parser.parse_args()

    fires = get_column(
        args.file_name,
        args.country_column,
        args.country,
        result_column=args.fires_column
    )
    print(fires)


if __name__ == "__main__":
    main()