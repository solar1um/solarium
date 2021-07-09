# Встроенная функция
# Built-in function
# print('Ulan')
# Выводит на экран все что внутри функции

#
# number = 10
# print(number)
# print('number')

# print(type(number))
# print(type(20))
# print(type(number) == type(20))

# print(type(20))
# print(type('20'))
# print(type(20) == type('20'))

# DATA TYPES
# Типы Данных

# 1) INT - INTEGER(ЦЕЛОЕ ЧИСЛО)
# 2) STR - STRING(СТРОКА)
# 3) FLOAT - FLOAT(ДЕСЯТИЧНОЕ ЧИСЛО)
# 4) LIST - LIST(СПИСОК)
# 5) TUPLE - TUPLE(КОРТЕЖ)
# 6) DICT - DICTIONARY(СЛОВАРЬ)
# 7) BOOL - BOOLEAN(БУЛЕВЫЕ)
# 8) FILES - FILES(ФАЙЛЫ)
# 9) SET - SET(СЕТЫ) ----- FROZENSET

# ОШИБКА
# x = 5
# y = '10'
# print(type(x), type(y))
# z = 10.2
# print(type(z))
# print(x + z)
# print(x + y)

######################STRINGS##################################

# word = 'WORLD oiajeroig ojrog 3oirjg3oi'
# print(word)
# print('WORLD')

# length
# ДАЕТ КОЛИЧЕСТВО СИМВОЛОВ В СТРОКЕ
# print(len(word))

# any_symbol = '!@#$%^&*()'
# print(type(any_symbol))

# sentence = "my favorite\t book\n is 'chippollino'   "
# length = len(sentence)
# print('length', length)
# print(type(length))
# print(type(sentence))
# print(type(len(sentence)))
# \t - табуляция
# \n - Новая строка
# print(sentence)

# print(dir(sentence))

# name = '   ulan temirlan a'
# print(name.capitalize())
# print(name.title())
# print(name.upper())

# name = ' UlAn tEmIRLan'
# print(name.title())
# print(name.lower())

# name = '?Ulan'
# print(name.startswith('!'))
# print(name.endswith('lan'))

# phrase = 'Shla Sasha po SHosse i sosala sushku'
# print(phrase.count('S'))
# print(phrase.count('s'))
# print(phrase.count(' '))
# print(phrase.count('Sasha'))

# phrase = 'Shla, Sasha po SHosse, i sosala sushku'
# print(phrase.split())
# print(phrase.split('s'))
# print(phrase.split(','))
# print(phrase.swapcase())

# String indexes Индексы строк

# name = 'Ulan Elena'
# print(name)
# print(len(name))
# print(name.find('w'))
# print(name[3])
# print(name[-3])

# Slices Слайсы
# <variable_name>[start:stop:step]
# name = 'Ulan Elena'

# print(name[::3])
# print(name[0::3])
# print(name[5:0:-2])

# Concatination Конкатинация
# print('1' + '2')
# print(5 * 'Ulan')

# name = input('Enter your name: ')
# print(type(name))
# print('You entered', name)
# print('You entered ' + name)

# x = 5
# print(type(x))
# y = x
# print(type(y))

# x = 'Ulan'
# print(type(x))
# y = int(x)
# print(y)
# print(type(y))

# name = input("Enter your name: ")
# print(name)

# age = int(input("Enter your age: "))
# print(type(age))
# print(age)

# amount = 100000
# money = int(input("Enter amount of money to withdraw: "))
# print(f"You have withdrawn {money} dollars")
#
# left = amount - money
# print("You have", left, "dollars")

"""
Create a program that displays your name and
complete mailing address. The address should be
printed in the format that is normally used
in the area where you live. Your
program does not need to read any input from the user.
"""

""" Stackoverflow """

"""
Write a program that asks the user to enter 
his or her name. The program should respond 
with a message that says hello to the user, using his or her name.
"""

# name = input("enter name: ")
# print('hello ' + name)
# print('hello', name)

"""
Write a program that asks the user to enter the 
width and length of a room. Once these values have 
been read, your program should compute and display the area of
the room. The length and the width will be entered as 
floating-point numbers. Include units in your prompt 
and output message; either feet or meters, depending on which
unit you are more comfortable working with.
"""

# length = float(input("Enter length of a room: "))
# width = float(input("Enter width of a room: "))
#
# area = length * width
# print('The area of a room is ' + str(area) + ' meters squared')

"""
Create a program that reads the length and
 width of a farmer’s field from the user in
feet. Display the area of the field in acres.
"""

# length = float(input("Enter length of a room: "))
# width = float(input("Enter width of a room: "))
#
# area = (length * width)/43560
# print('The area of a field is', round(area, 2), 'acres')

"""
In many jurisdictions a small deposit is 
added to drink containers to encourage people 
to recycle them. In one particular jurisdiction, 
drink containers holding one liter or less have a $0.10 deposit, 
and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of 
containers of each size from the user.
Your program should continue by computing 
and displaying the refund that will be
received for returning those containers. 
Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.
"""

"""
The program that you create for this exercise
will begin by reading the cost of a meal
ordered at a restaurant from the user. 
Then your program will compute the tax and
tip for the meal. Use your local tax rate when 
computing the amount of tax owing.
Compute the tip as 18 percent of the meal amount 
(without the tax). The output from
your program should include the tax amount, 
the tip amount, and the grand total for
the meal including both the tax and the tip. 
Format the output so that all of the values
are displayed using two decimal places.
"""

'''
ДЗ
# 7, 8, 9, 10 from book

2) Написать код, который принимает input() и возводит принятое число во вторую степень
3) Разделите одно целое число на второе, и результат округлите в большую сторону.
4) Разделите одно целое число на второе, и результат округлите в меньшую сторону.
'''

"""
ДЗ
1) Write a script that prints the last letter of a string.
Ex: 'hello!' # --> !
Ex: "Bishkek" --> k

2) Write a script that takes in a string and prints its length.
Ex: 'hello!' # --> 6
Такую функцию не проходили, но учимся гуглить!

3) Write a script that requires an input and prints out following:
"Hello, my name is: YOUR_NAME"
YOUR_NAME must be an input
Use concatenation

4) You are given a string.
In the first line, print the third character of this string.
In the second line, print the second to last character of this string.
In the third line, print the first five characters of this string.
In the fourth line, print all but the last two characters of this string.
In the fifth line, print all the characters of this string with even indices 
In the sixth line, print all the characters of this string with odd indices 
In the seventh line, print all the characters of the string in reverse order.
In the eighth line, print every second character of the string in reverse order, starting from the last one.
In the ninth line, print the length of the given string.

5) Given a string consisting of words separated by spaces. Determine how many words it has. To solve the problem, 
use the method count.
"""







###########################################
# EX1
#
# a = 'marx'
# lenght = len(a)
# lenght = int(lenght-1)
# print(a[lenght])


###########################################
#EX2

# str = 'hello'
# lenght = len(str)
# print(lenght)

###########################################
#EX3

# name = input('enter your name: ')
# print(f'hello my name is {name}')



###########################################

# EX4

# str  = 'dmitriy is cool'
# print(str[2])
# length = len(str)
# lenght = int(length)
# print(str[0:lenght])
# print(str[0:5])
# print(str[0:lenght - 2])
# print(str[1:lenght:2])
# print(str[0:lenght:2])
# print(str[0:lenght:-1])
# print(str[lenght: :-2])


###########################################

#EX5

# import math
# str = 'it is cool being rich'
# spaced = (str.count(' '))
# spaced = float(spaced)
# words_separated = spaced/2
# rounded = math.ceil(words_separated)
# print(rounded)


###########################################

#ex38

sides = int(input('enter the number of sides: '))
if sides == 3:
    print('triangle')
elif sides == 4:
    print('square')
elif sides == 5:
    print('pentagon')
elif sides == 6:
    print('hexagon')
elif sides == 7:
    print('heptagon')
elif sides == 8:
    print('octagon')
elif sides == 9:
    print('nonagon')
elif sides == 10:
    print('decagon')
else:
    print('quantity of sides out of range error 404')



##########################################


# mouth = input(
#     'enter the mouth: '
# )
# mouth = mouth.lower()
# if mouth :
#     leap = int(input('if it is leap year type "1", if not type "0"'))
#     if leap != 0:
#         print('29 days')
#     else:
#         print('28 days')


##########################################

#ex39


# mouth = input(
#     'print the mouth: '
# )
# mouth = mouth.lower()
# if mouth == 'january':
#     print('31 days')
# elif mouth == 'february':
#     leap = input('is now leap year? ')
#     if leap == 'yes':
#         print('29 days')
#     else:
#         print('28 days')
# elif mouth == 'march':
#     print('31 days')
# elif mouth == 'april':
#     print('30 days')
# elif mouth == 'may':
#     print('31 days')
# elif mouth == 'june':
#     print('30 days')
# elif mouth == 'july':
#     print('31 days')
# elif mouth == 'august':
#     print('31 days')
# elif mouth == 'september':
#     print('30 days')
# elif mouth == 'october':
#     print('31 days')
# elif mouth == 'november':
#     print('30 days')
# elif mouth == 'december':
#     print('31 days')
# else:
#     print('your mouth was typed wrong')

# lst = [1, [2,3,[4]], [2, [3]]]
# print(lst[-1][-1])

#########################################3
#ex40

# jackhammer = 130
# gas_lawnmower = 106
# alarm_clock = 70
# quiet_room = 40
#
# level = int(input('print the sound level in dB: '))
#
# if level < quiet_room:
#     print('level quiter than quiet room ')
# elif level == jackhammer:
#     print('such a jackhammer ')
# elif level < jackhammer and level > gas_lawnmower:
#     print('level between jackhammer and gas lawnmower')
# elif level < gas_lawnmower and level > alarm_clock:
#     print('level between gas lawnmower and alarm clock')
# elif level < alarm_clock and level > quiet_room:
#     print('level between alarm clock and quiet room')
# else:
#     print('level louder than jackhammer noise...')


###################################3

#ex41


# first_side =  int(input('print first side lenght: '))
# second_side = int(input('print second side lenght: '))
# third_side = int(input('print third side lenght: '))
#
# if first_side == second_side == third_side:
#     print('it is equilateral triangle')
# if first_side == second_side != third_side or first_side != \
#         second_side == third_side or first_side == \
#     third_side != second_side:
#     print('it is isosceles triangle')
# else:
#     print('it is scalene triangle ')


#######################################3
#ex42

# C4 = 261.63
# D4 = 293.66
# E4 = 329.63
# F4 = 349.23
# G4 = 392
# A4 = 440
# B4 = 493.88
#
# note = input('print the note: ')
#
# if note == 'C4':
#     print(C4)
# elif note == 'D4':
#     print(D4)
# elif note == 'E4':
#     print(E4)
# elif note == 'F4':
#     print(F4)
# elif note == 'G4':
#     print(G4)
# elif note == 'A4':
#     print(A4)
# elif note == 'B4':
#     print(B4)


##################################
#ex43

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392
A4 = 440
B4 = 493.88

frequency = float(input('enter frequency: '))

if frequency == 261.63:
    print('C4')
elif frequency < C4:
    print('lower than C4')
elif frequency > C4 and frequency < D4:
    print('between C4 and D4')
elif frequency > D4 and frequency < E4:
    print('between D4 and E4')
elif frequency > E4 and frequency < G4:
    print('between E4 and G4')
elif frequency > G4 and frequency < A4:
    print('between G4 and A4')
elif frequency > A4 and frequency < B4:
    print('between A4 and B4')
else:
    print('higher than B4')