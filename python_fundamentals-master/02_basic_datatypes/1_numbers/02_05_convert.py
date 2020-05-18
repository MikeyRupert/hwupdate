'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
g = 420
print(g)
g = g.__float__()
print(type(g))
print(g)
print(g.__float__())
print(type(g))
print(g)
g = int(g)
print(type(g))
print(g)
g = float(g)
print(type(g))
print(g)
q = g//5
print(type(q))
print(q)
w = g*q
print(w)
print(type(w))