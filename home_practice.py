list = [1293, 9849, 120]
list.insert(1, 100)
print(list)

# .count считает сколько раз что-то употребляляется в списке
# fruits = ["apple", "banana", "cherry"]
#
# x = fruits.count("cherry")
#
# print(x)


# age = input('enter your age in years: ')
# age = 365 * int(age)
# print(f'your age in days is {age}')


###################################

# import math
# import random
# random_numbers = random.randint(1000,9999)
# divided = random_numbers/12
# round_number = math.ceil(divided)
# print(f'random number is {random_numbers}')
# print(f'random number diveded by 12 is: {divided}')
# print(f'random number diveded by 12 and round to ceil is: {round_number}')



#####################################

# my_list = [500, 12, ['apple', ['banana', 'pineapple',
# 'coconut', ['python', 'javascript', ['usd', 'som'], 'orange']]]]
# print(my_list[-1][1][3][2][0])

#####################################





data_1 = [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1]
data_2 = [0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0]
sum_1 = (sum(data_1))
sum_2 = (sum(data_2))
bool = sum_1 == sum_2

print(f'sum of the numbers in data_1 and data_2 is equal: {bool}')
len_1 = len(data_1)
len_2 = len(data_2)
middle_1 = len_1/2
middle_2 = len_2/2
middle_1_round = round(middle_1)
middle_2_round = round(middle_2)
middle_1_round = int(middle_1_round)
middle_2_round = int(middle_2_round)

# Найдите средний индекс обоих списков
print('the middle number of first list is: ', data_1[middle_1_round])
print('the middle number of second list is: ', data_2[middle_2_round])
print('sum of the first list divided by 2 is:',sum_1/2)

######################################



integer_1 = input('print integer number (a): ')
integer_2 = input('print integer number (b): ')

sum = int(integer_1) + int(integer_2)
diff = int(integer_2) - int(integer_1)
product = int(integer_1) * int(integer_2)
quotient = int(integer_1) / int(integer_2)
reminder = int(integer_1) % int(integer_2)
log = 10 ** int(integer_1)
log_2 = int(integer_1) ** int(integer_2)

print(f'the sum of (a) and (b) is: {sum}')
print(f'the difference between (b) and (a) is {diff}')
print(f'the product of numbers is {product}')
print(f'the quotient of numbers is {quotient}')
print(f'the reminder when (a) is divided by (b) is{reminder}')
print(f'10 to the power of number (a) is {log}')
print(f'the result of the (a) to the power of (b) is: {log_2}')
