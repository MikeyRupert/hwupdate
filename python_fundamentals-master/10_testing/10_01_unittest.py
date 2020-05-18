'''
Demonstrate your knowledge of unittest by first creating a function with input parameters and a return value.

Once you have a function, write at least two tests for the function that use various assertions. The
test should pass.

Also include a test that does not pass.

'''
from math import pi

def circle(r):
    return pi*(r**2)

radii = [2,0,-3, 2 +5j,True, 'radius']
message = 'Area of circle with r = {radius} is {area}.'

for r in radii:
    A = circle(r)
    print(message.format(radius=r,area=A))
    