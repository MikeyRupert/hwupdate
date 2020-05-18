'''

Write the necessary code to display the area and perimeter of a rectangle that has a width of 2.4 and a height of 6.4.

'''
class Rectangle():
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width*self.height)

    def perimeter(self):
        return (2*(self.width+self.height))
    
    def __str__(self):
        return f'The area of the rectangle is {self.area()} and the perimeter is {self.perimeter()}.'
        
r = Rectangle(2.4,6.4)
print(r.__str__())