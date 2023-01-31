"""
Use Scoutfish for large scale filtering on a PGN file using the Python wrapper
for the engine.
"""
from scoutfish.scoutfish import Scoutfish

if __name__ == "__main__":
    # Specify a path for the Scoutfish executable, as it's in a separate
    # folder.
    scoutfish = Scoutfish(engine="scoutfish/scoutfish")
    scoutfish.setoption("threads", 10)
    PGN_PATH = ""
    PGN_PATH = "/Users/isaac/Downloads/ChessDBs/lichess_elite_2022-08.pgn"
    if not PGN_PATH:
        PGN_PATH = input("Directory of PGN file: ")
    if not PGN_PATH.endswith(".pgn"):
        raise ValueError(f"The following path isn't a PGN file: {PGN_PATH}")

    scoutfish.open(PGN_PATH)
    query = {"result": "0-1"}
    res = scoutfish.scout(query)
    print(res)
