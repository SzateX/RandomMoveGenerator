import numpy as np


class RankIndex:
    INDEXES = [RANK_1, RANK_2, RANK_3, RANK_4, RANK_5, RANK_6, RANK_7, RANK_8] = [i for i in np.arange(0, 8, dtype=np.uint64)]


class Ranks:
    [RANK_1, RANK_2, RANK_3, RANK_4, RANK_5, RANK_6, RANK_7, RANK_8] = [np.uint64(0xff) << (np.uint64(8) * i) for i in np.arange(0, 8, dtype=np.uint64)]