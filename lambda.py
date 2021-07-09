# def func_name():
#     print("hello")

#func_name()

# n = func_name
#
# n()

# def another_function(a):
#     print(f'{a}')
#
# func = another_function
#
# func(5)

# x = lambda a: a
#
# def func(a):
#     return a

# print(x(5))

# print((lambda c: c * 2)(4))
#
# def another_func(c):
#     return c * 2
#
# print(another_func(4)

# example = lambda a, b: a * b
#
# print(example(1, 2))

# s = lambda name: name [0] if name.startswith('A') else name[-1]
#
# print(s('Alex'))
# print(s('Olex'))
#
# def func(name):
#     if name.startswith('A'):
#         return name[0]
#     else:
#         return name[-1]
#
# print(func('Oleg'))
# print(func('Aleg'))

# ############ MAP
# lst = [1, 2, 3, 4, 5]
#
# x = lambda num: num ** 2
#
# # var =  (map(x, lst))
# var =  list(map(x, lst))
# print(var)

example1 = ['amna', 'dima',
            'emir', 'abdullah',
            'omurberk', 'elena',
            'maksat']

ex_fun = lambda x: x[:3]

print(list(map(ex_fun, example1)))

# func = lambda x: x[::-1]
# print(list(map(func, example1)))
# map применяет функцию к каждому аргументу

#через map делать гораздо круче

# s = []
# for i in example1:
#     s.append(i[::-1])
#
# print(s)


# ################ FILTER @@@@@@

# example1 = ['amna', 'dima',
#             'emir', 'abdullah',
#             'omurberk', 'elena',
#             'maksat']
#
# p = lambda x: x.startswith('a')
#
# print(list(filter(p, example1)))

#сверху более питонично

# ex = []
#
# for i in example1:
#     if i.startswith('a'):
#         ex.append(i)
# print(ex)


# example = [1, 2, 3, 4, 5]
#
# print(list(filter(lambda x: x % 2 == 0, example)))

# myTuple = ("John", "Peter", "Vicky")
#
# x = " ".join(myTuple)
#
# print(x)

# example = ['dima', 'dmitriy', 'dimasik', 'diman', 'dmitro']
# p = lambda x: len(x) == 4
# print(list(filter(p, example)))

# ************* REDUCE

from functools import reduce
# lst = [1, 2, 3, 4, 5]
# v = reduce(lambda x, y: x * y, lst)
#
# print(v)

# n = [15, 2, -10, 224, 0, 19]
# v = reduce(lambda x, y: x if x > y else y, n)
# a = reduce(lambda x, y: y if x > y else x, n)
# print(v)
# print(a)

matrix = [
    [2, 6, 7, 10],
    [3, 5, 4, 8],
    [4, 7, 6, 14],
    [4, 5, 2, 6]
]

# wer = reduce(lambda x, y: x if sum(x) > sum(y) else y, matrix)
# print(sum(wer))

# def find_max(a, b):
#     lst = []
#     for i in matrix:
#         lst.append(sum(i))
#
#     value = max(lst)
#     ind = lst.index(value)
#     return matrix[ind]
#
# wer = reduce(find_max, matrix)
# print(find_max)
# print(wer)

#HOME WORK:

# #1

# lst = [1, 2, 3, 4, 5]
#
# a = lambda x: "even" if x % 2 == 0 else "odd"
# b = list(map(a, lst))
#
# counter = b.count('even')
# counter1 = b.count('odd')
#
# print(f'in the list {counter} even numbers and {counter1} odd numbers.')

#2

# lst = [150, 240, -170, -30]
#
# func = lambda x: x if x > 0 else 0
# func2 = lambda x: x if x < 0 else 0
#
# a = list(filter(func, lst))
# b = list(filter(func2, lst))
#
# print(f'its a positive numbers list: {a}')
# print(f'its a negative numbers list: {b}')

#3

# lst = [-10, -20, 10, 20, 0]
#
# # func = lambda x: -1 if x < 0 else 1
# def func(x):
#     if x > 0:
#         x = 1
#     elif x < 0:
#         x = -1
#     elif x == 0:
#         x = 0
#     return(x)
#
# print(list(map(func, lst)))

#4

# string = 'улыбок тебе, дед Макар!'
# string1 = 'lol'
# def func(string):
#     if string == string[::-1]:
#         print(1 == 1)
#     else:
#         print(1 == 2)
#
# func(string)
# func(string1)

#5

# inp = input().split(' ')
# for i in inp:
#     inp.append(i)
