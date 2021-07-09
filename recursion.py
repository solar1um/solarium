# name = 'ulan'
# print(name)

# def print_name(name):
#     print(name)
#
# print_name('Ulan')

# def print_name():
#     name = 'Ulan'
#     print(name)
#
# print(locals())
# print(globals())



# def sample():
#     name = 'Ulan'
#     print(locals())
#
#     def test():
#         city = ' Bshk'
#         print(locals())
#         print(surname)
#         print(globals())
#
#     test()
# surname = 'aaaa'
# sample()
# print(globals())


#we can always reach out to these functions
# import builtins
# print(dir(builtins))

# language = 'python'
# URL = 'https://www.google.com/'
#
# def func():
#     address = 'toktogul str'
#
#     def func_2():
#         print(address)
#         print(language)
#         print(number)
#         print(URL)
#
#         i = 15

        # print(name)
        # pass

    # number = 10
    # func_2()
    # print(i)
    #name = 'ulan' WILL GIVE ERROR
# func()

# if True:
#     pass


# *************************** RECURSION РЕКУРСИИ **********8

# def test():
#
#     print('recursion')
#
#     test()
# #это есть рекурсия
# test()
#
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#
# print(factorial(10))

# def summa(n, total):
#     if n == 4:
#         return total
#     else:
#         return summa(n + 1, total + n)
#
# print(summa(1, 0))

# summa(2, 1)
# summa(3, 3)
# summa(4, 6)
# summa(5, 10)
# summa(6, 15)
# summa(7, 21)
# summa(8, 28)
# summa(9, 36)
# summa(10, 45)


#ex 173
# a = []
# while 1:
#     b = input('->')
#     if(len(b) > 0):
#         a.append(b)
#     else:
#         break
# print(sum(map(int, a)))

#or

# def summa():
#     i = input()
#     if i == '':
#         return 0
#     else:
#         total = summa() + int(i)
#     return total
#
# print(summa())
