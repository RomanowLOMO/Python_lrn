# # работа с аргументами функций, позиционные, непоз, параметры по умолчанию
# def config(gpu, ram, cpu='i7'):
#     return {'gpu': gpu, 'ram': ram, 'cpu': cpu}
#
#
# print(config(gpu='1050ti', ram='16gb', cpu='i9'))


# def works(arg):
#     res = []
#     res.append(arg)
#     return res
#
#
# print(works('a'))
# print(works('b'))
#
# def nobuggy(arg, res=None):
#     if res is None:
#         res = []
#     res.append(arg)
#     return res
#
#
# print(nobuggy('a'))
# print(nobuggy('b'))
#
# # позиционные аргументы через *
# def print_args(cpu, gpu, *args):
#     print('cpu: ', cpu)
#     print('gpu: ', gpu)
#     print('other: ', args)
#
#
# print_args('i7', 'gtx 1050ti', 4, 'fdfsf')
#
# # аргументы ключевые слова через **
# def print_kwargs(*args, **kwargs):
#     print('Keyword arg: ', kwargs)
#     print('other: ', args)
#
#
# print_kwargs(cpu='i7', gpu='gtx1050ti', ram='16gb')
#
# # строки документаци, удобночитаемость имеет значение!
# def echo(param):
#     """
#     function return input param
#     doc string
#     python 3.6
#     """
#     return param
#
#
# help(echo)
# print(echo.__doc__)
#
# # функция как объект класса
# def pr_answer():
#     print(42)
#
# def run_func(func):
#     func()
#
# run_func(pr_answer)
#
# def add_args(arg1, arg2):
#     print(arg1 + arg2)
#
#
# def run_something_with_args(func, arg1, arg2):
#     func(arg1, arg2)
#
#
# run_something_with_args(add_args, 1, 2)
#
# def sum_arg(*args):
#     print(sum(args))
#
#
# def run_with_pos_args(func, *args):
#     return func(*args)
#
#
# run_with_pos_args(sum_arg, 1, 2, 3, 4, 5)
#
# # функция внутри функции
# def outer(a, b):
#     def inner(c, d):
#         return c + d
#     return inner(a, b)
#
#
# outer(1, 2)
#
# def knights(saying):
#     def inner(quote):
#         return "We are the knights who say: '%s'" % quote
#     return inner(saying)
#
# print(knights('Hi'))
#
# # замыкания
# def knights2(saying):
#     def inner2():
#         return "We are the knights who say: '%s'" % saying
#     return inner2
#
#
# a = knights2('Hi')
# b = knights2('Bu')
#
# print(a())
# print(b())
# # лямбда функции
# def edit_story(words, func):
#     for word in words:
#         print(func(word))
#
#
# stairs = ['thud', 'meow', 'thud', 'hiss']
#
#
# # def enliven(word):
# #     return word.capitalize() + '!'
#
# edit_story(stairs, lambda word: word.capitalize() + '!')
#
a = ['abcde']