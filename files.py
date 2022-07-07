import numpy as np


def generate_file(index: np.uint64):
    value = np.uint64(0)
    for i in np.arange(0, 8, dtype=np.uint64):
        value |= np.uint64(1) << (i * np.uint64(8)) + index
    return value


class FileIndex:
    INDEXES = [A, B, C, D, E, F, G, H] = [i for i in np.arange(0, 8, dtype=np.uint64)]


class Files:
    [A, B, C, D, E, F, G, H] = [generate_file(i) for i in FileIndex.INDEXES]
    ALL = np.uint64(np.iinfo(np.uint64(0)).max)
    NONE = np.uint64(0)