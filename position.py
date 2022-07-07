import numpy as np

from color import Color
from pieces import PieceType
from ranks import Ranks
from squares import Squares


class Position(object):
    bitboards: np.ndarray = np.ndarray((len(Color), len(PieceType)), dtype=np.uint64)
    side_to_move: Color = Color.WHITE
    castling_rights: np.ndarray = np.ndarray((4,), dtype=np.bool)
    halfmove_clock: np.uint8 = np.uint8(0)
    en_passant: np.uint64 = np.uint64(0)

    def reset_position(self):
        self.bitboards[Color.BLACK][PieceType.PAWN] = Ranks.RANK_7
        self.bitboards[Color.WHITE][PieceType.PAWN] = Ranks.RANK_2
        self.bitboards[Color.BLACK][PieceType.KNIGHT] = Squares.B8 | Squares.G8
        self.bitboards[Color.WHITE][PieceType.KNIGHT] = Squares.B1 | Squares.G1
        self.bitboards[Color.BLACK][PieceType.BISHOP] = Squares.C8 | Squares.F8
        self.bitboards[Color.WHITE][PieceType.BISHOP] = Squares.C1 | Squares.F1
        self.bitboards[Color.BLACK][PieceType.ROOK] = Squares.A8 | Squares.H8
        self.bitboards[Color.WHITE][PieceType.ROOK] = Squares.A1 | Squares.H1
        self.bitboards[Color.BLACK][PieceType.QUEEN] = Squares.D8
        self.bitboards[Color.WHITE][PieceType.QUEEN] = Squares.D1
        self.bitboards[Color.BLACK][PieceType.KING] = Squares.E8
        self.bitboards[Color.WHITE][PieceType.KING] = Squares.E1

        self.side_to_move = Color.WHITE
        for i in range(4):
            self.castling_rights[i] = np.bool(True)
        self.halfmove_clock = np.uint8(0)
        self.en_passant = np.uint64(0)