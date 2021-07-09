# def decorator(f):
#     def innner():
#     # def wrapper():
#         lst = []
#         for i in range(0, 10):
#             lst.append(i)
#
#         print(lst)
#         print(f())
#
#     return innner
#
# @decorator
# def func():
#
#     return('Function 1')
#
#
# @decorator
# def func2():
#
#     return('Function 2')
#
#
#
# @decorator
# def func3():
#
#     return('Function 3')
#
# func()
# func2()
# func3()
import re
from datetime import datetime

file = open('scarlet.txt').read().strip()
# file = open('scarlet.txt').readlines()
# file = open('scarlet.txt').readline()
# print(type(file))



# def execution_time(func):
#     def wrapper():
#         start = datetime.now()
#         func()
#         end = datetime.now()
#
#         print(end - start, func.__name__)
#
#     return wrapper
#
#
# @execution_time
# def dictionary():
#     data = {
#         'e': 'Dima',
#         'E': 'Dima'
#     }
#     result = ''
#     for i in file:
#         result += data.get(i, i)
#
#     return result
#
#
# @execution_time
# def list_join():
#     result = []
#     for i in file:
#         if i in 'eE':
#             result.append('Ulan')
#         else:
#             result.append(i)
#
#     return ''.join(result)
#
#
# @execution_time
# def list_comprehension():
#     result = [i if i not in 'eE' else 'Ulan' for i in file]
#     return ''.join(result)
#
#
# @execution_time
# def str_replace():
#     result = file.replace('e', 'Ulan')
#     result = result.replace('E', 'Ulan')
#
#     return result
#
#
# @execution_time
# def map_lambda():
#     result = map(lambda i: i if i not in 'eE' else 'Ulan', file)
#     return ''.join(list(result))
#
#
# @execution_time
# def regex():
#     text = re.sub('[eE]', 'Ulan', file)
#     return text
#
#
# dictionary()
# list_join()
# list_comprehension()
# str_replace()
# map_lambda()
# regex()

import random

# def decorator(f):
#     def inner():
#
#     return inner()
#
# @decorator
# def logic():
#     string = 'i love coca-cola'
#     for i in string:
#         lst = [True, False]
#         a = random.choice(lst)
#         if a == True:
#             print(i.upper(), end = '')
#         else:
#             print(i, end = '')
#     return logic()
#
# print(decorator(logic()))


# def uppercase_randomly(funct):
#     def inner():
#         text = funct
#
#         lst_comp = [i.upper() if random.choice([0, 1])
#                     else i for i in text]
#         print(''.join(lst_comp))
#
#     return inner
#
# @uppercase_randomly
#
# def func():
#     return file

# ЧЕКНУТЬ В ФАЙЛЕ (НЕ РАБОТАЕТ)


# def get_one_element(funct):
#     def inner():
#         text = funct()
#
#         print(random.choice(text))
#
#     return inner
#
#
# @get_one_element
# def func():
#
#     return [1, 2, 'stroka', 123, ['a', 'b']]
#
# func()