'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''
import itertools
colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]
print((set([(color.title(),size)for color in colors for size in sizes])))
direct= [colors,sizes]
for i in itertools.product(*direct):
    print('\n',i)
    

