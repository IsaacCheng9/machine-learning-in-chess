"""
Convert a PGN file to a folder of Parquet files for the game metadata to make
it easier to perform data analysis with Dask and pandas.
"""
import csv
import multiprocessing
import os
from time import perf_counter

import chess.pgn
import dask.dataframe as dd

from merge_csv_files import merge_csv_files


def convert_pgn_metadata_to_csv_file(pgn_file: str, whitelisted_events: set) -> str:
    """
    Write the metadata of each game in a PGN file to a .csv file.

    Args:
        pgn_file: The path to the PGN file.
        whitelisted_events: The game types that we want to include in the CSV.

    Returns:
        The path of the output CSV file.
    """
    # Replace the .pgn extension with the .csv extension in the output file.
    csv_file_path = pgn_file.replace(".pgn", ".csv")
    # Avoid overwriting an existing file.
    while os.path.exists(csv_file_path):
        i = 1
        csv_file_path = csv_file_path.replace(".csv", f"({i}).csv")

    header = [
        "UTCDate",
        "UTCTime",
        "Event",
        "TimeControl",
        "Result",
        "Termination",
        "ECO",
        "Opening",
        "White",
        "Black",
        "WhiteElo",
        "BlackElo",
        "Site",
    ]
    print(f"Creating split CSV file: {csv_file_path}")

    start = perf_counter()
    with open(csv_file_path, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        with open(pgn_file, encoding="utf-8") as pgn:
            game = chess.pgn.read_game(pgn)
            while game:
                if (
                    # Exclude games involving a non-human player.
                    (
                        "black_title" in game.headers
                        and game.headers["black_title"] == "BOT"
                    )
                    or (
                        "white_title" in game.headers
                        and game.headers["white_title"] == "BOT"
                    )
                    # Exclude games that were abandoned.
                    or (
                        "Termination" in game.headers
                        and game.headers["Termination"] == "Abandoned"
                    )
                    # Exclude games that aren't a time control category
                    # (event) that we want.
                    or (game.headers["Event"] not in whitelisted_events)
                ):
                    # Avoid writing the game to the CSV file and move onto the
                    # next game.
                    game = chess.pgn.read_game(pgn)
                    continue

                row = [
                    game.headers["UTCDate"],
                    game.headers["UTCTime"],
                    game.headers["Event"],
                    game.headers["TimeControl"],
                    game.headers["Result"],
                    game.headers["Termination"],
                    game.headers["ECO"],
                    game.headers["Opening"],
                    game.headers["White"],
                    game.headers["Black"],
                    game.headers["WhiteElo"],
                    game.headers["BlackElo"],
                    game.headers["Site"],
                ]
                writer.writerow(row)
                game = chess.pgn.read_game(pgn)
    end = perf_counter()

    print(f"Created split CSV file: {csv_file_path} in {end - start:.3f} seconds")
    return csv_file_path


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
    WHITELISTED_EVENTS = {
        "Rated Blitz game",
        "Rated Rapid game",
    }
    # The number of files the PGN file has been split into.
    NUM_SPLIT_FILES = 6
    PGN_PATH = ""
    if not PGN_PATH:
        PGN_PATH = input("Directory of PGN file: ")
    if not PGN_PATH.endswith(".pgn"):
        raise ValueError(f"The following path isn't a PGN file: {PGN_PATH}")

    print(f"Converting PGN file: {PGN_PATH} to CSV file...")
    # Remove the '.pgn' extension from the PGN file path.
    BASE_FILE_PATH = PGN_PATH.replace(".pgn", "")
    # Convert each split PGN file to a CSV file.
    with multiprocessing.Pool() as pool:
        # Track the paths of the CSV files that were created so they can be
        # merged later.
        csv_file_paths = pool.starmap(
            convert_pgn_metadata_to_csv_file,
            [
                (f"{BASE_FILE_PATH}_{i}.pgn", WHITELISTED_EVENTS)
                for i in range(1, 1 + NUM_SPLIT_FILES)
            ],
        )
    # Merge the split CSV files into one.
    combined_csv = merge_csv_files(f"{BASE_FILE_PATH}.csv", csv_file_paths)

    # Convert the CSV file to a folder of Parquet files.
    convert_csv_to_parquet(combined_csv)
