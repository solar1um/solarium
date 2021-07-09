# print('word' == 'word')

# if 'word' == 'word':
#     print('word equals word')


# x = 7
# y = 10
# if x + y == 15:
#     print('equals 15')
# elif x + y == 16:
#     print('equals 16')
# else:
#     print('else')


#  x = True
#
# if x:
#     print('yes')



# x = 10
# y = 11
# if x > y:
#     print('x > y')
# elif x == y:
#     print('x == y')
# elif x < y:
#     print('x < y')
# else:
#     print('else')


# name = 'ulan'
# names = ['amna', 'dima', 'elena', 'emir', 'ulan','omurbek']

# print(names.index(name))

# print(name in names)

# if name in names:
#     print(names.index(name))
#
# letter = 'b'
# letters = ['qweasdzxc']

# print(letter in letters)
# if letter in letters:
#     print(letter.index(letter))

# age = int(input('enter your age: '))
# status = (input('enter your age: ')
# if age < 18:
#     if status != 'VIP':
#         print('not allowed')
#     else:
#         print('welcome')
# else:
#     print('welcome')

# age = int(input('enter your age: '))
# status = input('enter the pass: ')
# if age < 18:
#     if status != '123':
#         print('not allowed')
#     else:
#         print('allowed')
#     print('not allowed')
# else:
#     print('allowed')




# < > <= >= == !=
# and or not

# x = 5
# y = 4
# if x + y == 9 and (x + y) % 3 == 0:
#     print('yes')


# print(not(False))
# переворачивает false на tгue и на оборот
# x = 5
# y = 10
#
# if not(x + y) == 15:
#     print('done')

# year = int(input('enter the year: '))
# year = year % 4
# if year == 0:
#     print('it is leep year')
# else:
#     print('this year is not leep')
#
# output = 'leap' if year % 4 == 0 else 'not leap'
# print(output)


# given_number = int(input('enter the number: '))
# if given_number % 3 == 0 and given_number % 5  == 0:
#     print('HahaHoo')
# elif given_number %3 == 0:
#     print('Haha')
#
# elif given_number %5 == 0:
#     print('Hoo')
#
# else:
#     print('Aaaaa')


# first = input('enter the number: ')
# second = input('enter the number: ')
#
# if first == second:
#     print('this numbers are equal ')
# else:
#     print('this numbers arent equal')




# i = int(input('enter number: '))
# if i % 3 == 0 and i % 5 == 0:
#     print('HahaHoo')
# elif i % 3 == 0:
#     print('Haha')
# elif i % 5 == 0:
#     print('Hoo')
# else:
#     print('Aaaaa')


# a = int(input('first one: '))
# b = int(input('second one: '))
# c = int(input('third one: '))
#
# if a == b == c:
#     print('whole numbers is equal')
# elif a == b:
#     print('a equals b')
# elif b == c:
#     print('b equals c')
# elif a == c:
#     print('a equals c')
# else:
#     print('nothing is coinside')



# a = int(input('print some number: '))
# b = int(input('print some number: '))
# if a + b == 5:
#     print("sum of numbers equals 5")
# elif a + b < 5:
#     print("sum of the numbers less than 5")
# elif a + b > 5:
#     print("sum of the numbers more than 5")


# word = input('enter some word: ')
# if word[0] == 'a' or 'e' or 'i' or 'o' or 'u' or 'y':
#     print(f'an {word}')
# else:
#     print(f'a {word}')

word = input('enter some word: ')
vowels = 'aioue'
if word[0].lower() in vowels:
    print(f'An {word}')
else:
    print(f'A {word}')


# years = int(input('print how many years: '))
# if years < 1:
#     print('enter not negative number or 0')
# else:
#     print(f'{years * 7} dog years.')


