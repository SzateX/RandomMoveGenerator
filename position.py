import numpy as np

from bit_manipulations import ffs
from color import Color
from files import Files
from move import Move, MoveType
from pieces import PieceType
from ranks import Ranks
from squares import Squares

from collections import deque


class Position(object):
    bitboards: np.ndarray = np.ndarray((len(Color), len(PieceType)), dtype=np.uint64)
    side_to_move: Color = Color.WHITE
    castling_rights: np.ndarray = np.ndarray((4,), dtype=np.bool_)
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
            self.castling_rights[i] = np.bool_(True)
        self.halfmove_clock = np.uint8(0)
        self.en_passant = np.uint64(0)

    def get_pseudovalid_moves(self):
        opponent = np.uint64(1) - self.side_to_move.value
        current_pieces = np.bitwise_or.reduce(self.bitboards[self.side_to_move])
        opponent_pieces = np.bitwise_or.reduce(self.bitboards[opponent])
        all_pieces = current_pieces | opponent_pieces
        valid_moves = deque()

        mask = np.uint64(1)
        index = np.uint8(0)
        while mask:
            if current_pieces & mask:
                if self.bitboards[self.side_to_move][PieceType.PAWN] & mask:
                    pawn = self.bitboards[self.side_to_move][PieceType.PAWN] & mask
                    pawn_direction = np.int8(8) - np.int8(16) * self.side_to_move.value
                    forward_push = np.uint64(np.int64(pawn) << np.int64(pawn_direction))
                    next_index = ffs(forward_push)
                    if forward_push & Ranks.RANK_1_8:
                        # promotions
                        if not forward_push & all_pieces:
                            # push promotions
                            valid_moves.append(Move(index, next_index, MoveType.QUEEN_PROMOTION))
                            valid_moves.append(Move(index, next_index, MoveType.ROOK_PROMOTION))
                            valid_moves.append(Move(index, next_index, MoveType.BISHOP_PROMOTION))
                            valid_moves.append(Move(index, next_index, MoveType.KNIGHT_PROMOTION))
                        if not pawn & Files.A and (forward_push >> np.uint64(1)) & opponent_pieces:
                            # left captures promotions
                            valid_moves.append(Move(index, next_index - 1, MoveType.QUEEN_PROMOTION_CAPTURE))
                            valid_moves.append(Move(index, next_index - 1, MoveType.ROOK_PROMOTION_CAPTURE))
                            valid_moves.append(Move(index, next_index - 1, MoveType.BISHOP_PROMOTION_CAPTURE))
                            valid_moves.append(Move(index, next_index - 1, MoveType.KNIGHT_PROMOTION_CAPTURE))
                        if not pawn & Files.H and (forward_push << np.uint64(1)) & opponent_pieces:
                            # right captures promotions
                            valid_moves.append(Move(index, next_index + 1, MoveType.CAPTURE))
                            valid_moves.append(Move(index, next_index + 1, MoveType.CAPTURE))
                            valid_moves.append(Move(index, next_index + 1, MoveType.CAPTURE))
                            valid_moves.append(Move(index, next_index + 1, MoveType.CAPTURE))
                    else:
                        # normal pushes
                        if not forward_push & all_pieces:
                            valid_moves.append(Move(index, next_index, MoveType.QUITE_MOVE))
                        if not pawn & Files.A and (forward_push >> np.uint64(1)) & opponent_pieces:
                            # left captures
                            valid_moves.append(Move(index, next_index - np.uint64(1), MoveType.CAPTURE))
                        if not pawn & Files.H and (forward_push << np.uint64(1)) & opponent_pieces:
                            # right captures
                            valid_moves.append(Move(index, next_index + np.uint64(1), MoveType.CAPTURE))
                        if not pawn & Files.A and forward_push & Ranks.RANK_3_6 and forward_push >> np.uint64(1) & self.en_passant:
                            # left en passant
                            valid_moves.append(Move(index, next_index - np.uint64(1), MoveType.EN_PASSANT))
                        if not pawn & Files.H and forward_push & Ranks.RANK_3_6 and forward_push << np.uint64(1) & self.en_passant:
                            # right en passant
                            valid_moves.append(Move(index, next_index + np.uint64(1), MoveType.EN_PASSANT))
                    if np.uint64(np.int64(pawn) >> np.int64(pawn_direction)) & Ranks.RANK_1_8:
                        # double pushes
                        double_forward = np.uint64(np.int64(pawn) << (np.int64(pawn_direction) * np.int64(2)))
                        if not forward_push & all_pieces and not double_forward & all_pieces:
                            valid_moves.append(Move(index, ffs(double_forward), MoveType.DOUBLE_PAWN_PUSH))
                    print("PAWN")
                elif self.bitboards[self.side_to_move][PieceType.KNIGHT] & mask:
                    print("KNIGHT")
                elif self.bitboards[self.side_to_move][PieceType.BISHOP] & mask:
                    print("BISHOP")
                elif self.bitboards[self.side_to_move][PieceType.ROOK] & mask:
                    print("ROOK")
                elif self.bitboards[self.side_to_move][PieceType.QUEEN] & mask:
                    print("QUEEN")
                elif self.bitboards[self.side_to_move][PieceType.KING] & mask:
                    print("KING")
                print(hex(mask))
            mask = mask << np.uint64(1)
            index += np.uint8(1)
        print(hex(current_pieces))
        print(hex(opponent_pieces))
        print(hex(all_pieces))

        return valid_moves

