'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
import random
num = random.randint(1,100_000_000)
print(num)
guess = int(input('number-->'))
while num < guess or guess < num:
    

