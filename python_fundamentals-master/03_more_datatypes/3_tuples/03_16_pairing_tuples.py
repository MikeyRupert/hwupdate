'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
def num(n):
    n = sorted(n)
    i = iter(n)
    for w in zip(i,i):
        if len(n)%2==0:
            print(w)
        else:
            n.append(0)
            print(w)
list_ = [23,32,32,2,34,4,2,2,0,3,43,2]
(num(list_))