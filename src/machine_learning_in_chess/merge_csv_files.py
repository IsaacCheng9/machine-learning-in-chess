"""
A utility script to that takes the input of multiple CSV files, and outputs
both a single CSV file and a folder of Parquet files. This can be useful when
aggregating the results of performing multiprocessing on a split data set.
"""
import csv
from time import perf_counter
from typing import List

import dask.dataframe as dd
from tqdm import tqdm


def merge_csv_files(output_file_name: str, csv_files: List[str]) -> str:
    """
    Merge the multiple CSV files into one.

    Args:
        output_file_name: The name of the output CSV file.
        csv_files: The paths to the split CSV files.

    Returns:
        The path of the combined CSV file.
    """
    print(f"\nMerging {len(csv_files)} CSV files into {output_file_name}")

    start = perf_counter()
    with open(output_file_name, "w", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        header_written = False
        for split_csv_file in tqdm(csv_files):
            with open(split_csv_file, encoding="utf-8") as file:
                reader = csv.reader(file)
                # Add the header row from the first CSV file.
                if not header_written:
                    header = next(reader)
                    writer.writerow(header)
                    header_written = True
                else:
                    next(reader)
                for row in tqdm(reader):
                    # Avoid adding the row if it's the header row.
                    if row[0] == "UTCDate":
                        continue
                    writer.writerow(row)
    end = perf_counter()

    print(f"Merged CSV files into: {output_file_name} in {end - start:.3f}s")
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
    print(f"\nConverting the following CSV file to Parquet files: {csv_file}")
    df = dd.read_csv(
        csv_file,
        parse_dates={"UTCDateTime": ["UTCDate", "UTCTime"]},
        dtype={
            "Event": "category",
            "TimeControl": "string[pyarrow]",
            "Result": "category",
            "Termination": "category",
            "ECO": "string[pyarrow]",
            "Opening": "string[pyarrow]",
            "White": "string[pyarrow]",
            "Black": "string[pyarrow]",
            "WhiteElo": "int16",
            "BlackElo": "int16",
            "Site": "string[pyarrow]",
        },
    )
    df.to_parquet(parquet_folder)
    print(f"Converted CSV file to Parquet files: {parquet_folder}")
    return parquet_folder


if __name__ == "__main__":
    OUTPUT_FILE = ""
    if not OUTPUT_FILE:
        OUTPUT_FILE = input("Name of the output file (without extension): ")
    SPLIT_CSV_FILES = []
    while True:
        csv_file = input(
            f"Path to a CSV file to merge (currently merging {len(SPLIT_CSV_FILES)} - "
            "leave blank to finish): "
        )
        if not csv_file:
            break
        SPLIT_CSV_FILES.append(str(csv_file))

    # Merge the split CSV files into one.
    combined_csv = merge_csv_files(f"{OUTPUT_FILE}.csv", SPLIT_CSV_FILES)
    # Convert the CSV file to a folder of Parquet files.
    convert_csv_to_parquet(combined_csv)
