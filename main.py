from position import Position

import numpy as np

if __name__ == '__main__':
    pos = Position()
    pos.reset_position()
    valid_moves = pos.get_pseudovalid_moves()
    print(valid_moves)
    print(len(valid_moves))
