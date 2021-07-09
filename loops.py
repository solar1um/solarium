#while / for loops

# x = 5
# while x < 10:
#     print(x)
#     x = x + 1

# t = True
# while t:
#     print('this is true')
#     t = False


# numbers = [1, 2, 3, 4, 5]
# x = 0
# while x < len(numbers):
#     print(x)
#     x += 1


# numbers = [209, 2398, 12, 1298, 134]
# x = 0
#
# while x < len(numbers):
#     print(numbers[x], end='\t')
#     x += 1



# numbers = [1, 2, 3, 4, 5, 6, 7]
# i = 0
# while i < len(numbers):
#     print(numbers[i] ** 2)
#     i += 1

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# i = 0
# while i < len(numbers):
#     if numbers[i] % 2 == 0:
#         print(numbers[i])
#     i += 1


# print(list(range(0, 101, 2)))

# i = 0
# while i < len(list(range(0, 1000))):
#     print(i)
#     i += 1


# lst = list(range(0, 1000))
# i = 0
# while i < len(lst)
#     print(i)
#     i += 1







# names = ['anma', 'dima', 'elena', 'abdullah',
#          'maksat', 'omurbek', 'emir', 'amirkhan']
#
# i = 0
# while i < len(names):
#     if names[i].endswith('a'):
#         print(names[i])
#     i += 1


# names = ['anma', 'dima', 'elena', 'abdullah',
#          'maksat', 'omurbek', 'emir', 'amirkhan']




# i = 0
# while i < 10:
#     print(i)
#     i += 1
#
# lst = list(range(10))
# for i in lst:
#     print(i)
#
# print('a' in 'Ulan')



# for i in range(10):
#     print(i ** 2)



# names = ['anma', 'dima', 'elena', 'abdullah',
#          'maksat', 'omurbek', 'emir', 'amirkhan']
#
# for i in names:
#     print(i.upper())
#
# for index, name in enumerate (names):
#     print(index, name)




# words = ['key', 'home', 'time', 'work']
# for word in words:
#     print(word[-1])
#
# i = 0
# while i < len(words):
#     print(words[i][-1])
#     i += 1


# n = int(input('enter the number: '))
# for i in range(0, n, 2):
#     print(i)


# names = ['amna', 'dima', 'elena', 'abdullah',
#          'maksat', 'omurbek', 'emir', 'amirkhan']
#
# for i in names:
#     if i.startswith('a'):
#         print(i[::-1])
#     else:
#         print(i[-1])


# mess = [1, 2, 3, '4', '5', '6', 7, 8, '9', 10]
#
# for i in mess:
#     if type(i) == str:
#         i = int(i)
#         print(i ** 2)
#     else:
#         print(i)

# dont work
# n = 0
# lst = []
#
# while n != 0:
#     n = int(input('enter number: '))
#     if n != 0:
#         lst.append(n)
#
# print(lst)






# sum = 0
# i = 0
# while True:
#     n = int(input())
#     if n != 0:
#         sum = sum + n
#         i += 1
#     else:
#         break
# print(sum/i)


# prices = [4.95, 9.95, 14.95, 19.95, 24.95]
# for price in prices:
#     print(price)


# prices = [4.95, 9.95, 14.95, 19.95, 24.95]
# for price in prices:
#     discount = round(price * 0.6, 2)
#     final_price = round(price - discount, 2)
#     print(price, discount, final_price)


# print (range(0, 100))

# n = 5
# for i in range(0, n + 1):
#     # print(i)
#     for j in range(1, i + 1):
#         print(j, end = ' ')
#     print()

# n = int(input())
# summa = 0
# for num in range(1, n + 1):
#     summa = summa + num
#
# print(f'sum of first {n} numbers is: {summa}')




# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
#
# for i in list1:
#     if i > 150:
#         break
#     if i % 5 == 0:
#         print(i)



# number = 75869
# print(len(str(number)))

# counter = 0
# while number != 0:
#     number = number // 100
#     counter +=1
#
# print(counter)


# lst = ''
# num = 5
# for i in range(num, 0, -1):
#     for j in range(num, 0, -1):
#         print(j, end = ' ')
#     print()
#     num -= 1

# for i in list1[::-1]:
#     print(i)


# start = 25
# end = 50
# a = range(25, 50)
# for i in a:
#     if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
#         print(i)


# t = 10
# i = 0
# num1, num2 = 0, 1
#
# while i != t:
#     print(num1)
#     temp = num1 + num2
#     num1 = num2
#     num2 = temp
#
#     i += 1

i = 0
while i != 10:
    print('dima')
    i = i + 1