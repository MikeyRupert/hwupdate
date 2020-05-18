'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
from math import pi

def cir_area(r):
    if r< 0 :
        raise ValueError("need to get a tad bit higher")
    return pi*(r**2) 

radii = [2,0,-3, 2 +5j,True, 'radius']
message = 'Area of circle with r = {radius} is {area}.'

for r in radii:
    A = cir_area(r)
    print(message.format(radius=r,area=A))
    
