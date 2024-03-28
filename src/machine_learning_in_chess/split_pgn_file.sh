# Split a PGN file into multiple files:
# $1: Path of PGN file to split
# $2: Maximum number of chess games per file (default 1,000,000)
./pgn-extract/pgn-extract -#${2:-1000000} $1