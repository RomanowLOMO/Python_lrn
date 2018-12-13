import unittest
import itertools


def rle(iterable):
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


class Test(unittest.TestCase):
    def test_rle(self):
        self.assertEqual(rle("mississippi"), [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2), ('i', 1), ('p', 2), (
            "i", 1)])

    def test_rle_empty(self):
        self.assertEqual(list(rle("")), [])


if __name__ == "__main__":
    unittest.main()
