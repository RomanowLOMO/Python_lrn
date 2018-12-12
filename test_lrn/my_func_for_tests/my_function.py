import itertools


def rle(iterable):
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)
