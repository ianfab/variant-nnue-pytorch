RANKS = 8
FILES = 8
SQUARES = RANKS * FILES
KING_SQUARES = RANKS * FILES
PIECE_TYPES = 6
PIECES = 2 * PIECE_TYPES
USE_POCKETS = False
POCKETS = 2 * FILES if USE_POCKETS else 0

PIECE_VALUES = {
    1 : 126,
    2 : 781,
    3 : 825,
    4 : 1276,
    5 : 2538,
}