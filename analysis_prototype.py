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
    engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")
    stockfish = Stockfish("/opt/homebrew/bin/stockfish")
    pgn_file = "/Users/isaac/Downloads/lichess_db_standard_rated_2022-08.pgn"
    pgn = open(pgn_file, encoding="utf-8")

    for _ in range(1):
        game = chess.pgn.read_game(pgn)
        print(game)
        print()
        # Get the FEN string of the final board position.
        while game.next():
            game = game.next()
        fen = game.board().fen()
        print(fen)
        print()

    show_board_state(fen)
    info, top_five_moves = analyse_position(fen)
    pprint(info)
    print()
    pprint(top_five_moves)
