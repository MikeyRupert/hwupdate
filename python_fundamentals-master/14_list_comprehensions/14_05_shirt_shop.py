'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

# print(list(zip(color,size) for color in ["neon orange", "spring green"] for size in ["S", "M", "L"]))

    
import itertools
for cartesian_products in (itertools.product(["neon orange", "spring green"],["S", "M", "L"])):
    print('Earth Day Shirts - [color,size] :',[i.title() for i in cartesian_products])

