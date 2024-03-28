# Machine Learning to Study Patterns in Chess Games

A final year project for the University of Exeter, using data mining and machine
learning to understand patterns in chess games over the scale of millions of
games (~350 GB).

Ranked 1st in the cohort for undergraduate projects, with a final grade of 85%.

Supervisor: Chico Camargo

## Project Description

[Demonstration Video](https://www.youtube.com/watch?v=Vh1dLE22Oy8)

Chess, one of the oldest and most popular board games, has recently seen
large-scale exploration driven by online platforms like Lichess and Chess.com.
This study uses data mining and machine learning techniques to analyse millions
of games from the Lichess Open Database to uncover patterns and insights into
how people play chess. We created a data pipeline for efficient processing,
explored data features and distribution, and performed feature engineering. We
implemented classification models to predict game outcomes, a regression model
to investigate opening popularity and game outcomes, and k-means clustering to
group openings by game outcomes and mean differences in their variations. Our
models and clusters were analysed for their usefulness and evaluated for their
ability to provide insights into chess game patterns. Through this evaluation,
we assessed their success, limitations, and potential improvements. This study
demonstrates the potential of data mining and machine learning techniques in
uncovering patterns and insights in chess, contributing to growing research. By
understanding how people play chess, we can develop better tools, strategies,
and educational resources, enhancing fairness and enjoyment for players
worldwide.

## Data Pipeline

![Data Pipeline](https://github.com/IsaacCheng9/machine-learning-in-chess/assets/47993930/42717fd5-a921-424c-ad46-05fc99d73c48)

## Installation

We use Poetry for package management. Run the following the project root,
[machine-learning-in-chess](/) directory:

```shell
poetry install
```

## External Libraries

### pgn-extract

[pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) is a
command-line tool written in C that is used to manipulate chess databases
(formatted as PGN files) with millions of games.

#### Compiling pgn-extract

Before we can use pgn-extract, we must compile it from the source code:

1. Download the source code from the
   [pgn-extract website](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/).
2. Open the terminal and navigate to the source code directory for pgn-extract.
3. Compile the program by running: `make`
4. pgn-extract should now be compiled and ready to use via the `pgn-extract`
   file in the source code directory.

#### Splitting a PGN File with pgn-extract

We will use pgn-extract to split a PGN file into six smaller PGN files –
this enables us to take a sample of games from the larger PGN file, and then
process the smaller PGN files in parallel.

1. Open the terminal and navigate to the source code directory for pgn-extract.
2. Run the following command, where `<NUM_GAMES>` is the maximum number of games
   per PGN file output and `<PGN_FILE>` is the absolute file
   path to the PGN file to split:

   ```shell
   ./pgn-extract -#<NUM_GAMES> "<PGN_FILE>"
   ```

   For example:

   ```shell
   ./pgn-extract -#1000000 "/Users/isaac/Downloads/lichess_db_standard_rated_2022-01.pgn"
   ```

3. The split PGN files will be saved as `1.pgn`, `2.pgn`, `3.pgn`..., `6.pgn` in
   the same directory as `pgn-extract`. We will only use the first six files
   that are output.
4. Rename the PGN files to the original PGN file name, but with a suffix
   `.<NUM>.pgn` indicating the number of the PGN file to ensure that it will
   work with `convert_pgn_to_parquet.py` later (e.g.
   `lichess_db_standard_rated_2022-01_1.pgn`,
   `lichess_db_standard_rated_2022-01_2.pgn`,
   `lichess_db_standard_rated_2022-01_3.pgn`, ...,
   `lichess_db_standard_rated_2022-01_6.pgn`).

## Usage and Reproducing the Results

### Analysis of Provided Data Set

For convenience, we have pre-processed a data set of 40,121,728 standard rated
games on Lichess from January 2022 to December 2022 (inclusive) and provided it
in the [resources/lichess_db_standard_rated_2022](/resources/lichess_db_standard_rated_2022)
directory. This is also the default data set used in the Jupyter Notebook where
we perform the analysis.

To run the analysis on the provided data set, run the code in
[analyse_chess_data.ipynb](/src/machine_learning_in_chess/analyse_chess_data.ipynb).

### Analysis of Different Data Sets

If you would like to use a different data set from the Lichess Open Database,
you can follow these steps to reproduce the results:

1. Download a data set from the
   [Lichess Open Database](https://database.lichess.org/#standard_games).
2. Decompress the data into a PGN file (.pgn) – instructions are provided on
   the Lichess Open Database page under the 'Decompress .zst' heading.
3. Split the PGN file into six smaller PGN files, each containing up to a
   specified number of games (e.g. 1,000,000) with pgn-extract.
   - See the section above for detailed instructions:
     [Splitting a PGN File with pgn-extract](#splitting-a-pgn-file-with-pgn-extract)
4. Extract the game metadata from PGN files to a CSV file and a folder of
   Parquet files by running
   [convert_pgn_to_parquet.py](/src/machine_learning_in_chess/convert_pgn_to_parquet.py)
   and providing the name of the original PGN file (before it was split, e.g.
   `lichess_db_standard_rated_2022-01.pgn`).
   - This will output a folder of Parquet files, as well as a CSV file that
     contains all the data (e.g. `lichess_db_standard_rated_2022-01.pgn` for the
     folder of Parquet files and `lichess_db_standard_rated_2022-01.csv`).
5. (Optional) If you want to use data sets from multiple months (like in our
   study), merge the CSV files from the previous step into a single CSV file and
   a folder of Parquet files by running
   [merge_csv_files.py](/src/machine_learning_in_chess/merge_csv_files.py) and
   providing the paths of the CSV files to merge.
6. Change the `DATA_PATH` variable to the path of the directory containing the
   Parquet files in
   [analyse_csv_data.ipynb](/src/machine_learning_in_chess/analyse_chess_data.ipynb),
   and then run the notebook.

### Manual Data Exploration

If you want to manually explore the data, we have provided a program to convert
the CSV output to an SQLite3 file (`.db`). This makes it easy to perform queries
and sorting, as the CSV file outputs may be too large to view directly.

1. Run [convert_csv_to_sqlite3.py](/src/machine_learning_in_chess/convert_csv_to_sqlite3.py).
2. Enter the path to the CSV file to convert
   (e.g. `lichess_db_standard_rated_2022-01.csv`).
3. View the output SQLite3 file (e.g. `lichess_db_standard_rated_2022-01.db`) in
   the database browser of your choice
   (e.g. [DB Browser for SQLite](https://sqlitebrowser.org/)).

## Future Work

### Scoutfish

[Scoutfish](https://github.com/mcostalba/scoutfish) is a tool written in C++
that is used to query chess databases (formatted as PGN files) with very high
speed.

#### Compiling Scoutfish

1. Download the source code from the
   [Scoutfish GitHub repository](https://github.com/mcostalba/scoutfish).
2. Open the terminal and navigate to the `src` directory in the source code for
   Scoutfish: `cd src`
3. Compile the program by running: `make build ARCH=x86-64`
4. Scoutfish should now be compiled and ready to use via the `scoutfish` file in
   the `src` directory.

#### Creating a Scoutfish Index

Before Scoutfish can be used to query a chess database, we must first create a
Scoutfish index for that database:

1. Open the terminal and navigate to the `src` directory in the source code for
   Scoutfish: `cd src`
2. Run the following command, where `<PGN_FILE>` is the absolute file path to
   the PGN:

   ```shell
   ./scoutfish make "<PGN_FILE>"
   ```

3. The Scoutfish index will be created in the same directory as the PGN file as
   a `.scout` file (e.g. the index for `lichess_db_standard_rated_2022-01.pgn`
   will be saved as `lichess_db_standard_rated_2022-01.scout`).

We can use the Scoutfish index to perform various queries. Further information
and examples can be found on the
[Scoutfish GitHub repository](https://github.com/mcostalba/scoutfish).
