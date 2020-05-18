'''
Create two classes that model a rectangle and a circle. The rectangle class should
be constructed by length and width while the circle class should be constructed by
radius.

Write methods in the appropriate class so that you can calculate the area (of the rectangle and circle),
perimeter (of the rectangle) and circumference of the circle.

'''
from math import pi

class Rectangle():
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    def perimeter(self):
        return 2*(self.length+self.width)
    def __str__(self):
        return (f"The area of the rectange is {self.area()} and the perimeter is {self.perimeter()}.")

class Circle(): 
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return pi*self.radius**2
    def circum(self):
        return 2*pi*self.radius
    def __str__(self):
        return (f"The area of the circle is {self.area()} and the circumference is {self.circum()}.")

rec = Rectangle(10,30)
cir = Circle(13)
print(cir.__str__())
print(rec.__str__())