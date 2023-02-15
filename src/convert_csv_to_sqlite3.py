"""
A utility script to convert a CSV file to an SQLite3 database. This can be
useful to make the data more accessible for user interaction when the CSV file
is too large to be loaded into memory.
"""
import sqlite3

import pandas as pd


def convert_csv_to_sqlite3(csv_path: str) -> None:
    """
    Convert a CSV file to a SQLite3 database to make it more accessible for
    user interaction when the CSV file is too large to be loaded in-memory.

    Args:
        csv_path: The path to the CSV file.
    """
    output_file = csv_path.replace(".csv", ".db")
    print(f"Converting the following file to an SQLite3 database: {csv_path}...")
    df = pd.read_csv(
        csv_path,
        low_memory=False,
    )
    df.to_sql(
        "games",
        con=sqlite3.connect(output_file),
        if_exists="replace",
        index=False,
    )
    print(f"Created SQLite3 database at: {output_file}")


if __name__ == "__main__":
    CSV_PATH = ""
    if not CSV_PATH:
        CSV_PATH = input("Directory of CSV file: ")
    if not CSV_PATH.endswith(".csv"):
        raise ValueError(f"The following path isn't a CSV file: {CSV_PATH}")

    convert_csv_to_sqlite3(CSV_PATH)
