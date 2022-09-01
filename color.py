from enum import Enum, IntEnum

import numpy as np


class Color(np.uint64, Enum):
    WHITE = np.uint64(0)
    BLACK = np.uint64(1)