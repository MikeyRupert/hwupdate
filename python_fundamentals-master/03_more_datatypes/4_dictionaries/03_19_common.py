'''
Write a script that takes the following two dictionaries and creates a new dictionary by combining
the common keys and adding the values of duplicate keys together. Please use For Loops to iterate 
over these dictionaries to accomplish this task.

Example input/output:

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}


'''
import itertools
import collections

dict_1 = {"a": 1, "b": 2, "c": 32}
dict_2 = {"a": 2, "b": 300 , "d": 2}

num_dict = collections.defaultdict(int)
for letter,number in itertools.chain(dict_1.items(),dict_2.items()):
    num_dict[letter] += number
    
print(dict(num_dict))

