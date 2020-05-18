'''
- Write a script with three classes that model everyday objects.
- Each class should have an __init__ method that sets attributes
    to a default value if values are not passed.
- Create at least two objects of each class using the __init__ method.
- Each object should have at least three attributes.
- Each class should have at least two class attributes.
- Create a print method in each class that prints out the attributes
    in a nicely formatted string.
- Include a __str__ method in each class.
- Overload the __add__ method in one of the classes so that it's possible
    to add attributes of two instances of that class using the + operator.
- Once the objects are created, change some of the attribute values.

Be creative. Have some fun. :)
Using objects you can model anything you want.
Cars, animals, poker games, sports teams, trees, beers, people etc...

workout app
'''
class Workout():

    def __init__ (self,name,date,work=''):
        self.name = name
        self.date = date
        self.work = work

    def __str__(self):
        return f'on {self.date} {self.name} did the workout {self.work}'

class Boxing(Workout):
    def __init__(self,name,date,work='',shadowbox ,heavybag ,speedbag):
        super().__init__(name, date, work)
        self.rounds = shadowbox
        self.heavy = heavy
        self.speedbag = speedbag
        
        
        

class Running(Workout):
    pass

class lifting(Workout):
    pass
m = Workout('mikey','5-15','boxing and running')
print(m.__str__())