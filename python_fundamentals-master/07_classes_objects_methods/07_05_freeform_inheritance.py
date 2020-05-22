'''
Build on your previous freeform exercise.

Create subclasses of two of the existing classes. Create a subclass of
one of those so that the hierarchy is at least three levels.

Build these classes out like we did in the previous exercises.

If you cannot think of a way to build on your freeform exercise,
you can start from scratch here.

We encourage you to be creative and try to think of an example of
your own for this exercise but if you are stuck, some ideas include:

- A Vehicle superclass, with Truck and Motorcycle subclasses.
- A Restaurant superclass, with Gourmet and FastFood subclasses.

'''

class Bank:
    def __init__(self,name,scrilla):
        self.name = name
        self.scrilla = scrilla
        
    def deposit(self,how_much):
        self.scrilla += how_much
        return f'Your new balance is {self.scrilla}.'
    def withdraw(self,amount):
        if self.scrilla >= amount:
            self.scrilla -=amount
            return f"Your new balance is {self.scrilla}."
        else:
            return f'Come on playa we know you aint got that kind of money'
    def __str__(self):
        if self.scrilla > 1000:
            return "We at Stratton Oakmont appreciate your service",f'{self.name} has a account balance : {self.scrilla}'
        elif 0 < self.scrilla < 200:
            return ("We at Stratton Oakmont think your broke as hell and need find new bank"),(f'with your {self.scrilla} dollar having ass...')

m = Bank("Mikey",10000)
print(m.__str__())
print(m.withdraw(9900))
print(m.__str__())
print(m.withdraw(1000))
print(m.deposit(1000))
print(m.__str__())
e = Bank('Emily',20)
print(e.__str__())
