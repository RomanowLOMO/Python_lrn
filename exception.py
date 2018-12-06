class MyException(Exception):
    def __init__(self, val, leng):
        self.val = val
        self.length = leng


try:
    my_str = input('Enter string: ')
    if len(my_str) < 3:
        raise MyException(my_str, len(my_str))


except MyException as err:
    print(MyException.__name__ + ' length string < {0}: {1}' .format(err.length, err.val))
else:
    print('OK')
