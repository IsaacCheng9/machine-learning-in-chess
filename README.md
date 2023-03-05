# Machine Learning to Study Patterns in Chess Games

A final year project for the University of Exeter, using machine learning to
understand patterns in chess games over the scale of millions of games.

Supervisor: Chico Camargo

## Project Description

Chess is a very good game for data mining. Computational databases containing
pre-calculated exhaustive analyses of chess endgame positions – known as endgame
tables – have become powerful analytical tools, profoundly advancing the chess
community's understanding of the space of possible solutions for a game. Modern
chess has also been supported by servers such as Lichess, an open-source
Internet chess server which includes a database containing over 3 billion chess
games, in a wide range of player abilities, recording both the moves of the game
and related metadata, such as the names of the players, the winner/loser, and
the date the game was played. While the literature on chess openings, endgames,
and other features is centuries-old, the terabyte-scale exploration of different
games is much more recent.

The aim of this project is to apply data mining and machine learning tools to
chess databases such as Lichess mentioned above, to understand patterns in how
people play chess, and how the game works at the scale of millions or billions
of matches.

Questions we might ask include:

- What are the most common openings and the most common endgames?

- Do particular openings often lead to particular endgames?

- Which strategies work, and which ones do not?

- How does the popularity of different styles change over time?

- What's the best counter against a particular strategy?

- Is it possible to cluster similar chess matches?

- Does that match the classification into openings and endings?

- How does one do dimensionality reduction and classification on a chess match?

This project will require some basic knowledge of chess (or interest in picking
up that knowledge), but most of all, interest in data mining and machine
learning. In addition to providing a good opportunity for the development and
application of data science tools, this project should make a contribution to
the understanding of chess endgames, but also to studies of computational social
science and cultural analytics.

## External Libraries Used

### Scoutfish

[Scoutfish](https://github.com/mcostalba/scoutfish) is a tool written in C++
that is used to query chess databases (formatted as PGN files) with very high
speed.

### pgn-extract

[pgn-extract](https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/) is a
command-line tool written in C that is used to manipulate chess databases
(formatted as PGN files) with millions of games.

## Installation

### Python Versions

This project has been developed and tested to work on Python 3.9 onwards.

### Installing Dependencies

1. Ensure that you're in the root directory: `machine-learning-in-chess`
2. Install the Python dependencies: `pip install -r requirements.txt`

## Reproducing the Results

### Game Metadata Analysis

1. Download a data set from the [Lichess Open Database](https://database.lichess.org/#standard_games).
2. Decompress the data into a PGN file (.pgn) -- instructions are provided on
   the Lichess Open Database page under the 'Decompress .zst' heading.
3. Split the PGN file into multiple smaller PGN files, each containing up to a
   specified number of games (e.g. 1,000,000) with pgn-extract.
4. Extract the game metadata from PGN files to Parquet files by running
   `convert_pgn_to_parquet.py` and providing the name of the original PGN file
   (before it was split).
5. Change the `DATA_PATH` variable to the path of the directory containing the
   Parquet files in `analyse_csv_data.ipynb`, and then run the notebook.
