'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''


def func():
    string_user_input = input('String input: ')
    letter = input('Letter input: ')
    g = string_user_input.find(letter)
    print(f'Result: {g}')
func()
     