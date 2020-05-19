'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
'''person, amount tp taken tom green effect,empty shelfs due to one person seeing another person take extra tp then next person takes twice as much and so on'''
def my_enumerate(toilet_paper):
      for sharmin in enumerate(toilet_paper,start=1):
            yield sharmin
gen = my_enumerate(i**2 for i in range(4))
print(gen)
print('person:amout tp bought=',next(gen))
print(next(gen))
print(gen)
print(next(gen))
print('restart generator or will hit a wall ~~ StopIteration')
gen = my_enumerate(i**2 for i in range(4))
print(next(gen))
print(next(gen))
print(next(gen))