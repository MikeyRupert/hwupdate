'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
s = 'more python programming please'
print('\n',s)
s = s.replace('m','#')
print('\n',s)