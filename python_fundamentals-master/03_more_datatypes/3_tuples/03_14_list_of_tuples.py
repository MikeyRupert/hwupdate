'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
def list_of_tups():
    user_input = input('string hur\n\t==>')
    split_string = (user_input.split(' '))
    a,b = split_string  
    split_string = [tuple(a),tuple(b)]
    print(split_string)
list_of_tups()