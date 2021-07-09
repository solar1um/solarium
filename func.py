# def summa():
    # print(5 + 6)


#вызов функции

# summa()

# def summa (a, b):
#     # print(a, b)
#     print(a + b)
#
# # summa()
# summa(1, 50)



#
# def summa(a = 2, b = 3):
#     print(a + b)
#
# summa()
# summa(5)
# summa(1, 10)

# def summa(a=2, b=3, c=None):
#     print((a + b) * c)
#
# summa(a=2, b=6, c=3)

# def func():
#     a = input('say hello ')
#     print(a)
#
# func()

# def func(num):
#     for i in range(0, num):
#         if i % 2 == 0:
#             print(i)
#
# func(13)


# def func(n):
#     return n * 2
#
# def high_func(f):
#     return f + 2
#
# print(high_func(func(3)))


# def name_list(lst):
#     new_lst = []
#     for i in lst:
#         new_lst.append(i.title())
#     print(new_lst)
#     return(new_lst)
#
#
#
#
# def cut_names(lst):
#     result = []
#     for i in lst:
#         result.append(i[0])
#     print(result)
#
# cut_names(name_list(['amna,', 'dima', 'emir']))



def validate(p, p2):
    """
    :param p:
    :param p2:
    :return:
    lalalaalalalalalal
    """
#     if type(p) != int and type(p) != str:
#         raise Exception
#
#     if p == p2:
#         print('correct')
#     else:
#         print('incorect')
#
# validate(1, 1)

# help(validate)


# def func(n):
#     if n > 0:
#         a = str(n)
#         print(a[-1])
#         return(a[-1])
#
# func(100)


# def func(n):
#     if n % 2 == 0:
#         print(f'{n} is even')
#     else:
#         print(f'{n} is odd')
#     return(n)
#
# func(2)


# def func(n):
#     for i in range(0, n):
#         print(i**2)
# func(4)


# def func(n):
#     if n == n[::-1]:
#         print(n)
#     else:
#         print('its not')
#
#
# func('lol')


#EX5


# import datetime
# from datetime import time
#
#
# def func(a, b, c):
#     try:
#         if datetime.date(a, b, c) == datetime.date(a, b, c):
#             print('True')
#     except Exception:
#         print('False')
#
# func(2004, 11, 16)




#ex 6


# def func(n):
#     d1 = n % 10
#     n = n // 10
#     d2 = n % 10
#     n = n // 10
#     print(n + d1 + d2)
#
#
# func(999)


# def func(n):
#     print(len(str(n)))
#
#
# func(1000)


#ex 8

#
# def func(user_input):
#     lst = user_input.split()
#     print(lst)
#
#
#
# func(input('enter the numbers through a space: '))



#ex 9


# def func(n):
#     try:
#         print(n)
#
#     except Exception:
#         print('cant be division by 0')
#
#
#
#
# func(100/0)


#ex85

# import math
#
# def func(a, b):
#     hypotenuse = a**2 + b**2
#     print (round(math.sqrt(hypotenuse)))
#     return (round(math.sqrt(hypotenuse)))
#
#
#
#
#
#
# func(6, 8)


#ex86

# def func(n):
#     fare = 4
#     way = ((n*1000) / 140) * 0.25
#     print(f'total fare is: {round(fare + way, 2)}$')
#
#
#
# func(10)


#ex 87

# def func(n):
#     cost = 10.95 + (2.95 * (n - 1))
#     print(cost)
#     return(cost)
#
# quantity = input()
# func(int(quantity))


#ex 88

# def median(num1, num2, num3):
#
#     lst = [num1, num2, num3]
#     lst.sort()
#
#     print(lst[1])
#
# a = int(input('enter numbers with spaces: '))
# b = int(input('enter numbers with spaces: '))
# c = int(input('enter numbers with spaces: '))
#
# median(a, b, c)

#ex 89

def ordinal(n):
    data = {
        1: 'first',
        2: 'second',
        3: 'third',
        4: 'fourth',
        5: 'fifth',
        6: 'sixth',
        7: 'seventh',
        8: 'eighth',
        9: 'ninth',
        10: 'tenth',
        11: 'eleventh',
        12: 'twelfth'
    }

    if not (n in range(1, 13)):
        print('enter the valid number')
    else:
        print(data.get(n))

inp = int(input('enter num between 1 and 12: '))
ordinal(inp)