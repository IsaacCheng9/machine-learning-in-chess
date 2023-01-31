"""
Convert a PGN file to a CSV file for the game info and a CSV file for the moves
to make it easier to perform data analysis.
"""
from converter.pgn_data import PGNData

if __name__ == "__main__":
    PGN_PATH = ""
    PGN_PATH = "/Users/isaac/Downloads/ChessDBs/lichess_elite_2022-08.pgn"
    if not PGN_PATH:
        PGN_PATH = input("Directory of PGN file: ")
    if not PGN_PATH.endswith(".pgn"):
        raise ValueError(f"The following path isn't a PGN file: {PGN_PATH}")

    pgn_data = PGNData(PGN_PATH)
    result = pgn_data.export()
    result.print_summary()
