"""
A utility script to merge multiple CSV files into one. This can be useful when
aggregating the results of performing multiprocessing on a split data set.
"""
import csv
import dask.dataframe as dd
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
                # Add the header row from the first CSV file.
                if not header_written:
                    header = next(reader)
                    writer.writerow(header)
                    header_written = True
                else:
                    next(reader)
                for row in reader:
                    # Avoid adding the row if it's the header row.
                    if row[0] == "UTCDate":
                        continue
                    writer.writerow(row)

    print(f"Merged CSV files into: {output_file_name}")
    return output_file_name


def convert_csv_to_parquet(csv_file: str) -> str:
    """
    Convert a CSV file to a folder of Parquet files to be read as a Dask
    DataFrame.

    Args:
        csv_file: The path to the CSV file.

    Returns:
        The path of the folder of Parquet files.
    """
    # Remove the .csv extension for the name of the folder of .parquet files.
    parquet_folder = csv_file.replace(".csv", "")
    print(f"Converting the following CSV file to Parquet files: {csv_file}")
    df = dd.read_csv(csv_file)
    df.to_parquet(parquet_folder)
    print(f"Converted CSV file to Parquet files: {parquet_folder}")
    return parquet_folder


if __name__ == "__main__":
    OUTPUT_FILE = ""
    if not OUTPUT_FILE:
        OUTPUT_FILE = input("Name of the output file (without extension): ")
    SPLIT_CSV_FILES = []
    if not SPLIT_CSV_FILES:
        SPLIT_CSV_FILES = [
            str(file)
            for file in input("List of CSV files to merge (space separated): ").split()
        ]

    merge_csv_files(f"{OUTPUT_FILE}.csv", SPLIT_CSV_FILES)
    convert_csv_to_parquet(f"{OUTPUT_FILE}.csv")
