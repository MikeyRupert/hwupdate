'''
Using list comprehension, create a list that contains the individual
letters using the word "CodingNomads".

For example:

word = "CodingNomads"
..your code
result_list = ['C', 'o', 'd', 'i', 'n', 'g', 'N', 'o', 'm', 'a', 'd', 's']

'''
word = "CodingNomads"
nomad_list = [char for char in word]
nomads_list = [char for char in 'CodingNomads']   
print('\ndecent list comprehension',nomad_list)
print('\nlittle better',nomads_list)
print("\ncat's pajamas",[char for char in 'CodingNomads'])
print()