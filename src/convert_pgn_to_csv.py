"""
Convert a PGN file to a CSV file for the game metadata to make it easier to
perform data analysis with pandas.
"""
import csv
import multiprocessing
import os
from typing import List

import chess.pgn


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
    with open(csv_file_path, "w", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)

        with open(pgn_file, encoding="utf-8") as pgn:
            game = chess.pgn.read_game(pgn)
            while game:
                # Exclude games involving a non-human player.
                if (
                    "black_title" in game.headers
                    and game.headers["black_title"] == "BOT"
                    or "white_title" in game.headers
                    and game.headers["white_title"] == "BOT"
                ):
                    game = chess.pgn.read_game(pgn)
                    continue
                if game.headers["Event"] not in whitelisted_events:
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

    return csv_file_path


def merge_csv_files(base_pgn_file: str, csv_files: List[str]) -> str:
    """
    Merge the multiple CSV files into one.

    Args:
        base_pgn_file: The path to the PGN file without the '.pgn' extension.
        csv_files: The paths to the split CSV files.

    Returns:
        The path of the combined CSV file.
    """
    print(f"Merging {len(csv_files)} CSV files into one...")
    with open(f"{base_pgn_file}.csv", "w", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        for i, split_csv_file in enumerate(csv_files):
            with open(split_csv_file, encoding="utf-8") as file:
                reader = csv.reader(file)
                # Skip the header row if it's not the first CSV file.
                if i != 1:
                    next(reader)
                for row in reader:
                    writer.writerow(row)

    print(f"Merged CSV files into: {base_pgn_file}.csv")
    return f"{base_pgn_file}.csv"


if __name__ == "__main__":
    WHITELISTED_EVENTS = {
        "Rated Bullet game",
        "Rated Blitz game",
        "Rated Rapid game",
    }
    # The number of files the PGN file is split into.
    NUM_SPLIT_FILES = 6
    PGN_PATH = ""
    PGN_PATH = "/Users/isaac/Downloads/ChessDBs/lichess_db_standard_rated_2022-09.pgn"
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
                (f"{BASE_FILE_PATH}.{i}.pgn", WHITELISTED_EVENTS)
                for i in range(1, 1 + NUM_SPLIT_FILES)
            ],
        )
    # Merge the split CSV files into one.
    merge_csv_files(BASE_FILE_PATH, csv_file_paths)
