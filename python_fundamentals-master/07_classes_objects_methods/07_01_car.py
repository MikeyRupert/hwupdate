'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class Car():

    def __init__(self,model,year,speed,max_speed):
        self.model = model
        self.year = year
        self.speed = 0
        self.max_speed = max_speed

    def accel(self):
         self.speed += 5
         return self.speed
         if self.speed >= self.max_:
             Print('engine about to explode')

    def deaccel(self):
        if self.speed != 0:
            self.speed -=5
        else:
            pass
    def model(self):
        print(str(self.model))

    def speed(self):
        print(str(self.speed))

    def __str__(self):
        return (f'\nCombiniing engineering excellence with a classic interpretation of style, the {self.year} {self.model} can really purr with a top speed {self.max_speed}mph.\n')

c = Car('Plymouth Hemi GTX convertible',1967,220,250)
# print(c.accel())
print(c.__str__())
# print(c.accel())
# print(c.accel())
