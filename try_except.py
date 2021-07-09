# print(5/0)
# print(name)

# try:
#      print(name)
# except:
#     print('name variable in not defined')
# #
#
# print('here is some code')


# try:
#     print(5 / 1)
# except Exception:
#     print('cannot divide by 0')

#когда срабатывает try срабатывает else тоже

# else:
#     print('no errors found')


# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print('cannot divide by 0')


# try:
#     print(5 / 0)
#     print('this is sparta'.startwith() )
#     print(name)
#     print('name')
# except ZeroDivisionError:
#     print('maybe startswith')
# except ZeroDivisionError:
#     print('cannot divide by 0')
# except Exception:
#     print('there is something wrong')
# else:
#     print('no errors found')
# finally:
#     print('try except completed')

#finally срабатывает всегда



# try:
#     print(5 / 0)
# except Exception:
#     print('0')


# friends = ['amna', 'emir', 'dima', 'omurbek', 'ulan', 'elena', 'abdulla', 'maksat', 'amirkhan']
#
# for friend in friends:
#     if friend == 'Ulan':
#         raise Exception
#     else:
#         print(friend)



# friends = ['amna', 'emir', 'dima', 'omurbek', 'ulan', 'elena', 'abdulla', 'maksat', 'amirkhan']
# try:
    # print(friends[8])
    # print(friends[9])
    # if 'Tima' not in friends:
    #     raise Exception
    # print(friend)
    # print(5 / 0)
# except (IndexError, NameError, ZeroDivisionError):
#     print('no such index or variable is not defined')
# except NameError:
#     print('variable is not defined')
# except Exception as e:
#     print('exception was raised')
#     print(e)


# name = input('enter your name')
#
# try:
#     if not name.istitle():
#         raise Exception
# except Exception:
#     name = name.title()
#
# print(name)

# i = 1
# while i <= 10:
#     print(i ** 2)
#     i += 1

# n = ' l     l  '
# print(n.lstrip())


# n = int(input().strip())
# if n >= 1 and n <= 100:
#     if n % 2 == 1:
#         print('Weird')
#     elif n % 2 == 0:
#
#         if n in range(2, 5):
#             print('Nor Weird')
#         elif n in range(6, 20):
#             print('Weird')
#     if n % 2 == 0 and n > 20:
#         print('Not Weird')

# n = int(input())
# if n >= 1 and n <= 100:
#     if n % 2 == 1:
#         print('Weird')
#     if n % 2 == 0 and n in range(2, 5):
#         print('Not Weird')
#     if n % 2 == 0 and n in range(6, 20):
#         print('Weird')
#     if n % 2 == 0 and n > 20:
#         print('Not Weird')

