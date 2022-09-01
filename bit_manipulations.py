def ffs(x):
    return (x ^ ~ - x).bit_count() - 1