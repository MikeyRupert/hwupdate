'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
# import re
# def counter():
#     vowels = 'aeiou'
#     index1 = {}
#     user_string_input = str(input('string'))
#     if user_string_input in vowels:
#         index1.viewitems(user_string_input.find(vowels))
# print(index1)

script = input('Write a script to find how many vowels it has\n\t-->')
script = script.lower()
occur = {i:0 for i in 'aeiou'}
# print(occur)
for letter in script:
           if letter in occur:
               occur[letter] += 1
for number, vol in occur.items():
    total = 0
    for num in occur.values():
        total +=num
    print(number,vol)
print(occur)
print(f'There are a total of {total} vowels in this string!')
    