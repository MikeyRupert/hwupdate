'''
Write a script that prints out all the squares of numbers from 1- 50

Use a for loop that demonstrates the use of the range function.

'''

for i in range(1,51,5):
    square = i**2
    print(i,'**2 = ',square)


squared = [i**2 for i in range(50,100,5)]
for w in squared:
    print(w)

