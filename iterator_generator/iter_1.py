# итератор, пример
num_list = ['a', 'b', 3, 4]
itr = iter(num_list)
# print(next(itr))

itr1 = num_list.__iter__()
# print(next(itr1))

# пример работы цикла for с итератором
book = {
    'title': 'The Langoliers',
    'author': 'Stephen King',
    'year': 1990
}

# for i in book:
#     print(i)
#
# it = iter(book)
# while True:
#     try:
#         i = next(it)
#         print(i)
#     except StopIteration:
#         break


# # напишем свой объект-итератор
from random import random
#
#
# class RandomIterator:
#     def __init__(self, k):
#         self.k = k
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i < self.k:
#             self.i += 1
#             return random()
#         else:
#             raise StopIteration
#
#
# x = RandomIterator(5)
# for i in x:
#     print(i)

# class DoubleIter:
#     def __init__(self, lst):
#         self.lst = lst
#         self.i = 0
#
#     def __next__(self):
#         if self.i < len(self.lst):
#             self.i += 2
#             return self.lst[self.i - 2], self.lst[self.i - 1]
#         else:
#             raise StopIteration
#
#
# class MyList(list):
#     def __iter__(self):
#         return DoubleIter(self)
#
#
# for pair in MyList([1, 2, 3, 4]):
#     print(pair)
#
# # Генератор
#
# # функция принимает на вход список чисел, возвращает список кубов
#
#
# def cube_numbers(nums):
#     cube_list = []
#     for i in nums:
#         cube_list.append(i**3)
#     return cube_list
#
#
# cubes = cube_numbers([1, 2, 3, 4, 5])
# print(cubes)

# перепишем тоже самое через генератор
# def cube_numbers_1(nums):
#     for i in nums:
#         yield(i**3)
#
#
# cubes = cube_numbers_1([1, 2, 3, 4, 5])
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))


# def simple_gen():
#     print('check 1')
#     yield 1
#     print('check 2')
#     yield 2
#     print('check 3')
#
#
# gen = simple_gen()
# x = next(gen)
# print(x)
# y = next(gen)
# print(y)

# def random_gen(k):
#     for z in range(k):
#         yield z
#
#
# gen = random_gen(3)
# for i in gen:
#     print(i)

