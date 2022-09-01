from enum import Enum, IntEnum
import numpy as np


class PieceType(np.uint64, Enum):
    PAWN = np.uint64(0)
    KNIGHT = np.uint64(1)
    BISHOP = np.uint64(2)
    ROOK = np.uint64(3)
    QUEEN = np.uint64(4)
    KING = np.uint64(5)