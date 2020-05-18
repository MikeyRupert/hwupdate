'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
from math import pi
class Cylinder():
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return format(pi*(self.radius**2)*self.height,'1.3f')

    def surface_area(self):
        return format((2*pi*self.radius+2*pi*self.radius**2), '1.3f')

    def __str__(self):
        return f'The volume of the cylinder is {self.volume()} and the surface area is {self.surface_area()}.'

c = Cylinder(pi,5)
# print(c.volume())
# print(c.surface_area())
print(c.__str__())