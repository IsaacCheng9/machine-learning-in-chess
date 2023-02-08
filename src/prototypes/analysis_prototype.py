"""
A prototype for analysing chess positions using the Stockfish engine.
"""
from datetime import datetime

import chess
import chess.engine
import chess.pgn
from stockfish import Stockfish


def analyse_position(fen: str, depth_limit=20) -> tuple:
    """
    Analyse a FEN position using Stockfish.

    Args:
        fen: The FEN string of the position to analyse.
        depth_limit: The depth limit for the Stockfish engine - larger values
                     take longer to compute.

    Returns:
        A dictionary containing the evaluation info and a dictionary of details
        of the top five moves.
    """
    board = chess.Board(fen)
    stockfish.set_fen_position(fen)
    info = engine.analyse(board, chess.engine.Limit(depth=depth_limit))
    top_five_moves = stockfish.get_top_moves(5)
    return info, top_five_moves


def show_board_state(fen: str) -> None:
    """
    Show the board state for a given FEN string.

    Args:
        fen: The FEN string of the position to show.
    """
    board = chess.Board(fen)
    print(
        "(Capitals indicates white pieces, lowercase indicates black pieces.)"
        f"\n{board}\n"
    )


def log_monthly_metadata_by_game_type(pgn_file: str, event: str) -> None:
    """
    Write the metadata for a PGN file that represents a database of chess games
    in a month to a .log file.

    Args:
        pgn_file: The path to the PGN file.
        event: The game type to log the metadata for.
    """
    game_type_annotation = event.split()[1].lower()
    log_file_name = (
        f"metadata_{game_type_annotation}_"
        f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
    )
    # Write the metadata to a log file.
    with open(log_file_name, "w", encoding="utf-8") as log_file:
        with open(pgn_file, encoding="utf-8") as pgn:
            game = chess.pgn.read_game(pgn)
            while game:
                if game.headers["Event"] == event:
                    log_file.write(f"{game.headers}\n")
                game = chess.pgn.read_game(pgn)


if __name__ == "__main__":
    STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"
    PGN_PATH = "/Users/isaac/Downloads/lichess_db_standard_rated_2022-08.pgn"
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    stockfish = Stockfish(STOCKFISH_PATH)
    whitelisted_events = [
        "Rated Blitz game",
        "Rated Rapid game",
        "Rated Bullet game",
    ]

    for game_type in whitelisted_events:
        log_monthly_metadata_by_game_type(PGN_PATH, game_type)

    # with open(PGN_PATH, encoding="utf-8") as pgn:
    #     game = chess.pgn.read_game(pgn)
    #     while game:
    #         print(1)
    #         print(game)
    #         print()
    #         # Get the FEN string of the final board position.
    #         while game.next():
    #             game = game.next()
    #         game_fen = game.board().fen()
    #         print(2)
    #         print(game_fen)
    #         print()
    #         print(3)
    #         show_board_state(game_fen)
    #         game_info, game_top_five_moves = analyse_position(game_fen)
    #         print(4)
    #         pprint(game_info)
    #         print()
    #         print(5)
    #         pprint(game_top_five_moves)
    #         game = chess.pgn.read_game(pgn)
