'''
Write a script that takes a tuple and turns it into a list.

'''
def script(list1):
    print(type(list1))
    print('You entered a tuple,')
    print(list1)
    list1 = (list(list1))
    print('\n',type(list1))
    print('and returned a list')
    print(list1)
    

script((2,3,4,3,2))