'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
from operator import mul
from functools import reduce
try :
    def mult_list():
        list_ = []
        for i in range(1,11):
            user_int_list = int(input('Enter a number, int \n\t-->'))
            list_.append(user_int_list)
            n= (max(list_))
        print('\n',f'The largest number you entered was {n}.')
        g = reduce(mul, list_)
        print(f'\nThe product of the 10 numbers you just entered is {g}.\n')
            
except ValueError as e:
    print('enter a number')

mult_list()



