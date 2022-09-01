import dataclasses
from enum import Enum

import numpy as np


class MoveType(np.uint8, Enum):
    QUITE_MOVE = np.uint8(0)
    DOUBLE_PAWN_PUSH = np.uint8(1)
    KING_CASTLE = np.uint8(2)
    QUEEN_CASTLE = np.uint8(3)
    CAPTURE = np.uint8(4)
    EN_PASSANT = np.uint8(5)
    KNIGHT_PROMOTION = np.uint8(8)
    BISHOP_PROMOTION = np.uint8(9)
    ROOK_PROMOTION = np.uint8(10)
    QUEEN_PROMOTION = np.uint8(11)
    KNIGHT_PROMOTION_CAPTURE = np.uint8(12)
    BISHOP_PROMOTION_CAPTURE = np.uint8(13)
    ROOK_PROMOTION_CAPTURE = np.uint8(14)
    QUEEN_PROMOTION_CAPTURE = np.uint8(15)


@dataclasses.dataclass
class Move:
    from_square: np.uint8
    to_square: np.uint8
    flags: MoveType