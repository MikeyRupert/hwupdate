'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
t = "hello world"
t=tuple(t)
for word in t:
    for char in word:
        g = tuple(char)
        result_list = [g]
    print(result_list,sep='',end=' ')
    
# result_list =[t]
# print(result_list)

            
