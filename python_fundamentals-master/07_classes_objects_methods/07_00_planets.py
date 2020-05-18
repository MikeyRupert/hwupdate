'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    def __init__(self,color,gases,distance=int):
        self.color = color
        self.gases = gases
        self.distance = distance

    def liveable(self):
        if self.color == 'blue' and self.distance<100:
            return (f'this planet has the right color {self.color} and is less then {self.distance} billion miles from its sun.')
        elif self.color == 'blue' or self.distance<100:
            return (f'this planet has the wrong color {self.color}  but is less then {self.distance} billion miles from its sun.')
        else:
            return ('Danger, not in kansas anymore!')

    def water(self):
        if self.color == 'blue':
            return True
        else:
            return ('mad max')
    def infoplant(self):
        if self.gases=='n2'and'o2':
            return('we can breath there')
        else:
            return('oh damn')

mars = Planet('red','ar',89)
print(mars.liveable())
print(mars.infoplant())
