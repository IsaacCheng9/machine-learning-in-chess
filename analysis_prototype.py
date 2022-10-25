import pprint

import chess
import chess.engine
import chess.pgn


def analyse_position(fen: str, depth_limit=20):
    """
    Analyse a FEN position using Stockfish.

    Args:
        fen: The FEN string of the position to analyse.
        depth_limit: The depth limit for the Stockfish engine - larger values
                     take longer to compute.

    Returns:
        A dictionary containing the evaluation info.
    """
    board = chess.Board(fen)
    info = engine.analyse(board, chess.engine.Limit(depth=depth_limit))
    return info


def show_board_state(fen: str):
    """
    Show the board state for a given FEN string.

    Args:
        fen: The FEN string of the position to show.
    """
    board = chess.Board(fen)
    print(
        f"(Capitals indicates white pieces, lowercase indicates black pieces.)\n{board}"
    )


pgn = open("/Users/isaac/Downloads/lichess_db_standard_rated_2022-08.pgn")
engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")

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
pprint.pprint(analyse_position((fen)))
