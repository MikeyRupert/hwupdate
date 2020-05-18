'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
user_num = int(input('number between 1 and 1,000,000,000\n\t-->'))
if user_num%3==0:
    print(f'{user_num} is divisble by 3')
elif not user_num%3==0:
    print('\t\ttis not div by 3')