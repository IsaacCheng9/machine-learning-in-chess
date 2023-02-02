import pandas as pd


if __name__ == "__main__":
    CSV_PATH = ""
    # CSV_PATH = "/Users/isaac/Downloads/ChessDBs/lichess_elite_2022-08_game_info.csv"
    if not CSV_PATH:
        CSV_PATH = input("Directory of CSV file: ")
    if not CSV_PATH.endswith(".csv"):
        raise ValueError(f"The following path isn't a CSV file: {CSV_PATH}")

    df = pd.read_csv(CSV_PATH)
    print(df.info())
    print(df)
