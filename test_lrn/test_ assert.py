from test_lrn.my_func_for_tests import my_function


# def test_rle():
#     #ТЕСТИРУЕМ С ПОМОЩЬЮ ASSERT
#     #УПАДЕТ ПОТОМУ ЧТО rle("...") не будет списком. Слева генератор, справа список
#     assert rle("mississippi") == [
#         ('m', 1), ('i', 1), ('s', 2), ('i', 1),
#         ('s', 2), ('i', 1), ('p', 2), ('i', 1)
#     ]
#
#
# def test_rle_empty():
#     assert not list(rle(""))

def test_rle():
    # ПЕРЕПИШЕМ ТЕСТЫ СВЕРХУ И ДОБАВИМ СООБЩЕНИЯ ОБ ОШИБКЕ
    actual = my_function.rle("mississippi")
    expected = [
        ('m', 1), ('i', 1), ('s', 2), ('i', 1),
        ('s', 2), ('i', 1), ('p', 2), ('i', 1)
    ]
    message = "{} != {}".format(actual, expected)
    assert actual == expected, message


def test_rle_empty():
    actual = list(my_function.rle(""))
    expected = []
    message = "{} != {}".format(actual, expected)
    assert actual == expected, message


test_rle()
test_rle_empty()
