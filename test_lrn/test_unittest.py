from test_lrn.my_func_for_tests import my_function
import unittest


class MyTest(unittest.TestCase):
    # группируем тесты в этом классе
    def test_rle(self):
        self.assertEqual(my_function.rle("mississippi"), [('m', 1), ('i', 1), ('s', 2), ('i', 1), ('s', 2), ('i', 1),
                                                          ('p', 2), ("i", 1)])

    def test_rle_empty(self):
        self.assertEqual(list(my_function.rle("")), [])


class MyTest2(unittest.TestCase):

    def test_rle_two(self):
        self.assertEqual((my_function.rle('')), [])


def suite():
    tests = unittest.TestSuite([
        MyTest(),
        MyTest2()
    ])
    return tests


if __name__ == "__main__":
    # unittest.main()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

