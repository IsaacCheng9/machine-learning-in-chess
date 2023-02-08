"""
A utility script to merge multiple CSV files into one. This can be useful when
aggregating the results of performing multiprocessing on a split data set.
"""
import csv
from typing import List


def merge_csv_files(output_file_name: str, csv_files: List[str]) -> str:
    """
    Merge the multiple CSV files into one.

    Args:
        output_file_name: The name of the output CSV file.
        csv_files: The paths to the split CSV files.

    Returns:
        The path of the combined CSV file.
    """
    print(f"Merging {len(csv_files)} CSV files into {output_file_name}")
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        header_written = False
        for split_csv_file in csv_files:
            with open(split_csv_file, encoding="utf-8") as file:
                reader = csv.reader(file)
                header = next(reader)
                # Add the header row from the first CSV file.
                if not header_written:
                    writer.writerow(header)
                    header_written = True
                for row in reader:
                    writer.writerow(row)

    print(f"Merged CSV files into: {output_file_name}")
    return output_file_name


if __name__ == "__main__":
    OUTPUT_FILE = ""
    if not OUTPUT_FILE:
        OUTPUT_FILE = input("Name of the output file: ")
    if not OUTPUT_FILE.endswith(".csv"):
        raise ValueError(f"The output file must be a CSV file: {OUTPUT_FILE}")
    SPLIT_CSV_FILES = []
    if not SPLIT_CSV_FILES:
        SPLIT_CSV_FILES = [
            str(file)
            for file in input("List of CSV files to merge (space separated): ").split()
        ]

    merge_csv_files(OUTPUT_FILE, SPLIT_CSV_FILES)
