'''
Demonstrate how to access and print the value of pi to the console.

'''
from math import pi

class Circle():
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return format(pi*self.radius**2,'.3f')
    def perimeter(self):
        return format(2*self.radius*pi,'.3f')
cypher = Circle(8)
print(f'It\'s alot easier to find the area {cypher.area()} and perimeter {cypher.perimeter()} for any circle when you imort math')
