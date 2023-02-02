import pandas as pd


def get_most_popular_opening_category(df: pd.DataFrame) -> pd.Series:
    """
    Get the most popular opening categories for the data sample.

    df: The data sample to get the most popular opening categories for.

    Returns:
    """
    return df["eco"].value_counts()


if __name__ == "__main__":
    CSV_PATH = ""
    # CSV_PATH = "/Users/isaac/Downloads/ChessDBs/lichess_elite_2022-08_game_info.csv"
    if not CSV_PATH:
        CSV_PATH = input("Directory of CSV file: ")
    if not CSV_PATH.endswith(".csv"):
        raise ValueError(f"The following path isn't a CSV file: {CSV_PATH}")

    # Check whether the DataFrame has been loaded correctly.
    df = pd.read_csv(CSV_PATH)
    print(df.info())
    print(df)

    print(get_most_popular_opening_category(df))
