# lst = [1, 2, 3, 4]
# # for i in lst:
# #     print(i)
#
# it = iter(lst)
# print(next(it))
# print(next(it))
# print(next(it))

# class MyIter:
#
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
#             return self.i
#         else:
#             raise StopIteration
#
#
# it = MyIter(3)
#
# t = iter(it)
# print(next(t))
# print(next(t))
# print(next(t))
# print(next(t))
#
# def simple_gen(k):
#     for i in range(k):
#         yield i
#
#
# t = simple_gen(3)
# print(next(t))
# print(next(t))

gen = (i*i for i in range(5))
print(next(gen))
print(next(gen))