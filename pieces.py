from enum import Enum
import numpy as np


class PieceType(Enum):
    PAWN = np.uint64(0)
    KNIGHT = np.uint64(1)
    BISHOP = np.uint64(2)
    ROOK = np.uint64(3)
    QUEEN = np.uint64(4)
    KING = np.uint64(5)