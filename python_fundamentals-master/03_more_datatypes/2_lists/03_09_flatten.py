'''
Write a script that "flattens" a list. For example:

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

'''

starting_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
def flat(starting_list):
    for x in starting_list:
        if isinstance(x, list):
            for x in flat(x):
                yield x
                
        else:
            yield x
            
        
print(list(flat(starting_list)))
