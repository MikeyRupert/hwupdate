'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
from collections import Counter
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [k for k, v in Counter(list_).items() if v == 1]
print(f'boring list\n\t-->{list_}')
print(f'This was hard but after some digging i found the unique list to be\n\t-->{unique_list}')

