#
# # три списка
# marxes = ['Groucho', 'Chico', 'Harpo']
# pythons = ['Chapman', 'Cleese', 'Gilliam', 'Jones', 'Palin']
# stooges = ['Moe', 'Curly', 'Larry']
#
# # созадим кортеж
# tuple_of_lists = marxes, pythons, stooges
# print(tuple_of_lists)
# # создадим список списков
# list_of_lists = [marxes, pythons, stooges]
# print(list_of_lists)
# # создадим словарь
# dict_of_lists = {
#     'Marxes': marxes,
#     'Pythons': pythons,
#     'Stooges': stooges
# }
# print(dict_of_lists)
#
# # многоуровневый словарь
# life = {
#     'animals': {
#         'cats': ['Henry', 'Grumpy', 'Lucy'],
#         'octopi': {},
#         'emus': {}
#     },
#     'plants': {},
#     'other': {}
# }
#
# print(list(life.keys()))
# print(life['animals'].keys())
# print(life['animals']['cats'])
#
# furry = True
# small = False
#
# if furry:
#     if small:
#         print('It is a cat.')
#     else:
#         print('It is a bear.')
# else:
#     if small:
#         print('It is a skink.')
#     else:
#         print('It is a human')
#
# # циклы while
# count = 1
# while count <= 5:
#     print(count)
#     count += 1
#
#
# # break перрывание
# while True:
#     stuff = input("String to capitalize [type q t0 quit]: ")
#     if stuff == "q":
#         break
#     print(stuff.capitalize())
#
# # continue
# while True:
#     value = input('Int, pls [q to quit]: ')
#     if value == 'q':
#         break
#
#     number = int(value)
#     if number % 2 == 0:
#         continue
#     print(number, "squared is", number * number)
#
# # check end circle
# numbers = [1, 4, 5]
# position = 0
# while position < len(numbers):
#     number = numbers[position]
#     if number % 2 == 0:
#         print('Found even num', number)
#         break
#     position += 1
# else:
#     print('No even num found')
#
# # for
# rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
# current = 0
# while current < len(rabbits):
#     print(rabbits[current])
#     current += 1
# напишем иначе, проход по списку
# rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
# for rabbit in rabbits:
#     print(rabbit)
# # проход по строке
# word = 'cat'
# for letter in word:
#     print(letter)
# проход по словарю
# accusation = {
#     'room': 'ballroom',
#     'weapon': 'lead pipe',
#     'person': 'Col. Mustard'
# }
#
# for i in accusation:
#     print(i)
#
# for i in accusation.values():
#     print(i)
#
# for i in accusation.items():
#     print(i)
#
# for j, i in accusation.items():
#     print(j, i)
#
# cheeses = []
# for i in cheeses:
#     print('Ttt', i)
#     break
# else:
#     print("O_o")
#
# # zip
# days = ['Monday', 'Tuesday', 'Wednesday']
# fruits = ['banana', 'orange', 'peach']
# drinks = ['coffee', 'tea', 'beer']
# desserts = ['tiramisu', 'icecream', 'pie', 'pudding']
#
# for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
#     print(day, drink, fruit, dessert)
# # объеденим кортежи и создадим словарь
# english = 'Monday', 'Tuesday', 'Wednesday'
# french = 'Lundi', 'Mardi', 'Mercredi'
#
# list_book = list(zip(english, french))
# book = dict(zip(english, french))
# print(list_book)
# print(book)
# STR 112
# # Включения
# number_list = []
# for i in range(1, 6):
#     number_list.append(i)
#     i += 1
# print(number_list)
# list_a = list(range(1, 6))
# a_list = [num for num in range(1,6) if num % 2 == 0]
rows = range(1, 4)
cols = range(1, 3)
# for i in rows:
#     for j in cols:
#         print(i, j)
cells = [(i, j) for i in rows for j in cols]
for a, b in cells:
    print(a, b)
# word = 'letters'
# letter_counts = {i: word.count(i) for i in word}
# print(letter_counts)
