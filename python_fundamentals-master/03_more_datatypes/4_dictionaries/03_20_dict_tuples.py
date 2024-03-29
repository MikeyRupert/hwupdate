'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!

'''

input_dict = {"item1": 5, "item2": 6, "item3": 1}
g = sorted(input_dict.items(), key = lambda x: x[1])
# input_tup = tuple(input_dict)
print('\n',g)
print()
flip_script = sorted((value, key) for (key,value) in input_dict.items())
print(R"''' flip da script '''",'\n')
print(f'{flip_script}\n')