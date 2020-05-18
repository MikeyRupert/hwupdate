'''

Write a script that removes all duplicates from a list.

'''
from collections import Counter

list_ = [1, 2, 3, 4, 3, 4, 5]
unique_list2 = [k for k, v in Counter(list_).items() if v == 1]
print(f'very unique->\tuse counter.items\n only if number in list is found only once:\t{unique_list2}\n')
print(f'semi unique->\tset(list)\n finds if number is in list at least once at adds to new list:\t{set(list_)}\n')