# lst  = []
#
# lst = [i for i in range(0, 10)]

# for i in range(0, 10):
#     lst.append(i)
#
#
# print(lst)



# lst_2 = [i for i in range(0, 10)]
# lst_2 = [i ** 2 for i in range(0, 10)]





# lst_2 = [i for i in range(0, 10) if i % 2 == 0]
# print(lst_2)


# names = ['Amna', 'dima', 'emir', 'elena', 'omurbek', 'abdullah', 'maksat', 'amir']
# lst = [name[0].upper() for name in names]
# print(lst)


# lst = [name[-1] for name in names if name.startswith('A')]
# print(lst)

# from datetime import datetime
#
# now = datetime.now()
# lst = []
#
# for i in range(0, 100000):
#     lst.append(i)
#
# done = datetime.now()
# for_difference = done - now
# print(for_difference)
#
#
# now_2 = datetime.now()
# lst_2 = [i for i in range (0, 100000)]
# done_2 = datetime.now()
# comprehension_difference = done_2 - now_2
# print(comprehension_difference)



# dictionary_comprehension

d = {1: 2, 3: 4, 5: 6}
# print(d.items())
# d_2 = {key + 5: value + 5 for key, value in d.items()}
# print(d_2)



# for key, value in d.items():
#     print(key, value)


#
# names = {1:'emir',
#          2: 'dima',
#          3: 'amna'}
# new_names = {key: value.upper() for key, value in names.items() if key % 2 == 0}
# print(new_names)


"""
Doubled:
    Given a list of numbers, write a list comprehension that produces a list of each number doubled.
        [1, 2, 3, 4, 5]
        [2, 4, 6, 8, 10]

Squared:
    Given a list of numbers, write a list comprehension that produces a list of the squares of each number.
        [1, 2, 3, 4, 5]
        [1, 4, 9, 16, 25]

Evens:
    Given a list of numbers, write a list comprehension that produces a list of only the even numbers in that list.
        [1, 2, 3, 4, 5]
        [2, 4]

Odds:
    Given a list of numbers, write a list comprehension that produces a list of only the odd numbers in that list.
        [1, 2, 3, 4, 5]
        [1, 3, 5]

Positives:
    Given a list of numbers, write a list comprehension that produces a list of only the positive numbers in that list.
        [-2, -1, 0, 1, 2]
        [1, 2]
"""


# lst = [1, 2, 3, 4, 5]
# new_lst = [i * 2 for i in lst]
# print(new_lst)
#
#
# new_lst_2 = [i ** 2 for i in lst]
# print(new_lst_2)
#
# new_lst_3 = [i for i in lst if i % 2 == 0]
# print(new_lst_3)
#
# new_lst_3 = [i for i in lst if i % 2 == 1]
# print(new_lst_3)
#
# lst_2 = [-2, -1, 0, 1, 2]
# new_lst_4 = [i for i in lst_2 if i > 0]
# print(new_lst_4)
#
#
#
# # else тернарно:
#
# lst = [i ** 2 if i % 2 == 0 else str(i) for i in range (0, 10)]
# print(lst)
#
# lst_2 = [i ** 2
#          if i % 2 == 0
#          else i ** 3
#         if i % 3 == 0
#         else str(i)
#          for i  in range(0, 10)]
# print(lst_2)


# names = ['amna', 'dima', 'emir', 'elena', 'omurbek', 'abdullah', 'maksat', 'amir']
# for name in names:
#     for letter in name:
#         print(letter)

# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]
#
# new_list = []
# for row in matrix:
#     for num in row:
#         new_list.append(num)
# print(
#     new_list
#       )

# lst_comp = [num *  for row in matrix for num in row]
# # lst_comp = [num * 10  for row in matrix for num in row]
# print(lst_comp)


"""
Selectively stringify nums:
    Given a list of numbers, write a list comprehension that produces a list of strings of each number that is divisible by 5.
        [25, 91, 22, -7, -20]
        ['25', '-20']
        


Words not 'the'
    Given a sentence, produce a list of the lengths of each word in the sentence, but only if the word is not 'the'.
        'the quick brown fox jumps over the lazy dog'
        [5, 5, 3, 5, 4, 4, 3]


    Given a string representing a word, 
    write a list comprehension that produces 
    a list of all the vowels in that word.
        'mathematics'
        ['a', 'e', 'a', 'i']

Vowels set:
    Given a string representing 
    a word, write a set 
    comprehension that 
    produces a set of 
    all the vowels in 
    that word.
        'mathematics'
        set(['a', 'i', 'e'])


Disemvowel:
    Given a sentence, 
    return the sentence with 
    all vowels removed.
        'the quick brown fox 
        jumps over the lazy dog'
        'th qck brwn fx jmps 
        vr th lzy dg'

Wiggle numbers:
    Given a list of number, return the list with 
    all even numbers doubled, and all odd numbers turned negative.
        [72, 26, 79, 70, 20, 68, 43, -71, 71, -2]
        [144, 52, -79, 140, 40, 136, -43, 71, -71, -4]
"""

# lst = [25, 91, 22, -7, -20]
#
# new_list = [i for i in lst if i % 5 == 0]
# print(new_list)


#
# lst_comp = [len(i) for i in a if i != 'the']
# print(lst_comp)

# s = ['this', 'is', 'SPARTA']
# string = ' '.join(s)
# print(string)
# print(' '.join(s))

# string = 'mathematics'
# vowels = 'aeai'
# new_string = [i for i in string if i in vowels]
# print(new_string)



# string = 'mathematics'
# vowels = 'aeai'
# new_string = [i for
#               i in set(string)
#               if i
#               in vowels]
# print(new_string)



sentence = 'the quick brown ' \
           'fox jumps over ' \
           'the lazy dog'
vowels = 'aeionuy'
new_sentence = [i for
                i in sentence
                if i not in
                vowels]
print(''.join(new_sentence))
#
#
#
data = [72, 26, 79, 70, 20, 68, 43, -71, 71, -2]

new_list = [i * 2 if i % 2 == 0 else str(i * -1) for i in data]
print(new_list)