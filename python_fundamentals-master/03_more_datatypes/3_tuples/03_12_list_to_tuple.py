'''
Write a script that takes a list and turns it into a tuple.

'''
def script(list1):
    print(type(list1))
    print('You entered a list,')
    print(list1)
    list1 = (tuple(list1))
    print('\n',type(list1))
    print('and returned a tuple')
    print(list1)
    

script([2,3,4,3,2])
