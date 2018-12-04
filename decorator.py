# # Пример декоратора, как функциии обертки
#
#
# def my_shiny_new_decorator(a_function_to_decorate):
#     # Внутри себя декоратор определяет функцию-"обёртку".
#     # Она будет (что бы вы думали?..) обёрнута вокруг декорируемой,
#     # получая возможность исполнять произвольный код до и после неё.
#
#     def the_wrapper_around_the_original_function():
#         # Поместим здесь код, который мы хотим запускать ДО вызова
#         # оригинальной функции
#         print("Я - код, который отработает до вызова функции")
#
#         # ВЫЗОВЕМ саму декорируемую функцию
#         a_function_to_decorate()
#
#         # А здесь поместим код, который мы хотим запускать ПОСЛЕ вызова
#         # оригинальной функции
#         print("А я - код, срабатывающий после")
#
#     # На данный момент функция "a_function_to_decorate" НЕ ВЫЗЫВАЛАСЬ НИ РАЗУ
#
#     # Теперь, вернём функцию-обёртку, которая содержит в себе
#     # декорируемую функцию, и код, который необходимо выполнить до и после.
#     # Всё просто!
#     return the_wrapper_around_the_original_function
#
#
# # Представим теперь, что у нас есть функция, которую мы не планируем больше трогать.
# @my_shiny_new_decorator
# def a_stand_alone_function():
#     print("Я простая одинокая функция, ты ведь не посмеешь меня изменять?..")
#
#
# a_stand_alone_function()
#


# def a_decorator_passing_arguments(function_to_decorate):
#     def a_wrapper_accepting_arguments(arg1, arg2):  # аргументы прибывают отсюда
#         print("Смотри, что я получил:", arg1, arg2)
#         function_to_decorate(arg1, arg2)
#
#     return a_wrapper_accepting_arguments
#
#
# # Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# # мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# # она передаёт их декорируемой функции
#
# @a_decorator_passing_arguments
# def print_full_name(first_name, last_name):
#     print("Меня зовут", first_name, last_name)
#
#
# print_full_name("Питер", "Венкман")

# def method_friendly_decorator(method_to_decorate):
#     def wrapper(self, lie):
#         lie = lie - 3  # действительно, дружелюбно - снизим возраст ещё сильней :-)
#         return method_to_decorate(self, lie)
#
#     return wrapper
#
#
# class Lucy(object):
#
#     def __init__(self):
#         self.age = 32
#
#     @method_friendly_decorator
#     def sayYourAge(self, lie):
#         print("Мне %s, а ты бы сколько дал?" % (self.age + lie))
#
#
# lu = Lucy()
# lu.sayYourAge(-3)

#
# def a_decorator_passing_arbitrary_arguments(function_to_decorate):
#     # Данная "обёртка" принимает любые аргументы
#     def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
#         print("Передали ли мне что-нибудь?:")
#         print(args)
#         print(kwargs)
#
#         # Теперь мы распакуем *args и **kwargs
#         function_to_decorate(*args, **kwargs)
#
#     return a_wrapper_accepting_arbitrary_arguments


# @a_decorator_passing_arbitrary_arguments
# def function_with_no_argument():
#     print("Python is cool, no argument here.")
#
#
# function_with_no_argument()
#
#
# @a_decorator_passing_arbitrary_arguments
# def function_with_arguments(a, b, c):
#     print(a, b, c)
#
#
# function_with_arguments(1, 2, 3)

# @a_decorator_passing_arbitrary_arguments
# def function_with_named_arguments(a, b, c, platypus="Почему нет?"):
#     print("Любят ли %s, %s и %s утконосов? %s" %\
#           (a, b, c, platypus))
#
#
# function_with_named_arguments("Билл", "Линус", "Стив", platypus="Определенно!")
#
#
# class Mary(object):
#
#     def __init__(self):
#         self.age = 31
#
#     @a_decorator_passing_arbitrary_arguments
#     def sayYourAge(self, lie=-3):  # Теперь мы можем указать значение по умолчанию
#         print("Мне %s, а ты бы сколько дал?" % (self.age + lie))
#
#
# m = Mary()
# m.sayYourAge()
# # выведет:
# # Передали ли мне что-нибудь?:
# # (<__main__ .Mary object at 0xb7d303ac>,)
# # {}
# # Мне 28, а ты бы сколько дал?

#
# # вызов декоратора с различными аргументами
# def decorator_maker():
#     print("Я создаю декораторы! Я буду вызван только раз: " +\
#           "когда ты попросишь меня создать тебе декоратор.")
#
#     def my_decorator(func):
#         print("Я - декоратор! Я буду вызван только раз: в момент декорирования функции.")
#
#         def wrapped():
#             print("Я - обёртка вокруг декорируемой функции. "
#                   "Я буду вызвана каждый раз когда ты вызываешь декорируемую функцию. "
#                   "Я возвращаю результат работы декорируемой функции.")
#             return func()
#
#         print("Я возвращаю обёрнутую функцию.")
#         return wrapped
#
#     print("Я возвращаю декоратор.")
#     return my_decorator
#
#
# # # Давайте теперь создадим декоратор. Это всего лишь ещё один вызов функции
# # new_decorator = decorator_maker()
#
# @decorator_maker()
# def simple_func():
#     print("Hey, i am a simple func! ")
#
#
# print("============================")
# simple_func()

#
# def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
#     print("Я создаю декораторы! И я получил следующие аргументы:", decorator_arg1, decorator_arg2)
#
#     def my_decorator(func):
#         print("Я - декоратор. И ты всё же смог передать мне эти аргументы:", decorator_arg1, decorator_arg2)
#
#         # Не перепутайте аргументы декораторов с аргументами функций!
#         def wrapped(function_arg1, function_arg2):
#             print("Я - обёртка вокруг декорируемой функции.\n"
#                   "И я имею доступ ко всем аргументам: \n"
#                   "\t- и декоратора: {0} {1}\n"
#                   "\t- и функции: {2} {3}\n"
#                   "Теперь я могу передать нужные аргументы дальше"
#                   .format(decorator_arg1, decorator_arg1,
#                           function_arg1, function_arg2))
#             return func(decorator_arg1, decorator_arg2)
#
#         return wrapped
#
#     return my_decorator
#
#
# @decorator_maker_with_arguments("Леонард", "Шелдон")
# def decorated_function_with_arguments(function_arg1, function_arg2):
#     print("Я - декорируемая функция и я знаю только о своих аргументах: {0}"
#           " {1}".format(function_arg1, function_arg2))
#
#
# decorated_function_with_arguments("Раджеш", "Говард")