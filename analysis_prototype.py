import chess
import chess.engine
import chess.pgn

pgn = open("/Users/isaac/Downloads/lichess_db_standard_rated_2022-08.pgn")
engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")

for _ in range(1):
    game = chess.pgn.read_game(pgn)
    print(game)
