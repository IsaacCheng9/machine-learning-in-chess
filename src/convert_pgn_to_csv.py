"""
Convert a PGN file to a CSV file for the game metadata to make it easier to
perform data analysis with pandas.
"""
import csv
import os

import chess.pgn


def convert_pgn_metadata_to_csv_file(pgn_file: str, whitelisted_events: set) -> None:
    """
    Write the metadata of each game in a PGN file to a .csv file.

    Args:
        pgn_file: The path to the PGN file.
        whitelisted_events: The game types that we want to include in the CSV.
    """
    # Replace the .pgn extension with the .csv extension in the output file.
    csv_file_name = pgn_file.replace(".pgn", ".csv")
    # Avoid overwriting an existing file.
    while os.path.exists(csv_file_name):
        i = 1
        csv_file_name = csv_file_name.replace(".csv", f"({i}).csv")

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
    with open(csv_file_name, "w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
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


if __name__ == "__main__":
    WHITELISTED_EVENTS = {
        "Rated Blitz game",
        "Rated Rapid game",
        "Rated Bullet game",
    }
    PGN_PATH = ""
    PGN_PATH = "/Users/isaac/Downloads/ChessDBs/lichess_db_standard_rated_2022-08.1.pgn"
    if not PGN_PATH:
        PGN_PATH = input("Directory of PGN file: ")
    if not PGN_PATH.endswith(".pgn"):
        raise ValueError(f"The following path isn't a PGN file: {PGN_PATH}")

    convert_pgn_metadata_to_csv_file(PGN_PATH, WHITELISTED_EVENTS)
