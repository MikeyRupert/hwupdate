'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated fffto pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
user_input = input('Civilian~Name\n\t-->')
pig_name = user_input[1:]+user_input[0]+'ay'
print(f'Code~Name\n\t-->{pig_name}')