import numpy as np

from color import Color
from pieces import PieceType


class Position(object):
    bitboards = np.ndarray((len(Color), len(PieceType)), dtype=np.uint64)
    side_to_move = Color.WHITE
    castling_rights = np.ndarray((4,), dtype=np.bool)
    halfmove_clock = np.uint8(0)
    en_passant = np.uint64(0)


    def reset_position(self):
        pass