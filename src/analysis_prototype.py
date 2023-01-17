"""
A prototype for analysing chess positions using the Stockfish engine.
"""
from pprint import pprint

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


if __name__ == "__main__":
    STOCKFISH_PATH = "/opt/homebrew/bin/stockfish"
    PGN_PATH = "/Users/isaac/Downloads/lichess_db_standard_rated_2022-08.pgn"

    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    stockfish = Stockfish(STOCKFISH_PATH)

    with open(PGN_PATH, encoding="utf-8") as pgn:
        for _ in range(1):
            game = chess.pgn.read_game(pgn)
            print(game)
            print()
            # Get the FEN string of the final board position.
            while game.next():
                game = game.next()
            game_fen = game.board().fen()
            print(game_fen)
            print()
            show_board_state(game_fen)
            game_info, game_top_five_moves = analyse_position(game_fen)
            pprint(game_info)
            print()
            pprint(game_top_five_moves)
