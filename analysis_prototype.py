import pprint

import chess
import chess.engine
import chess.pgn

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

# Get the final position of the board using the FEN.
board = chess.Board(fen)
print("(Capitals indicates white pieces, lowercase indicates black pieces.)")
print(board)
print()
# Evaluate the final board position using Stockfish, limiting the depth to
# prevent the engine from taking too long.
info = engine.analyse(board, chess.engine.Limit(depth=20))
# Pretty print the evaluation info for ease of reading.
pprint.pprint(info)
