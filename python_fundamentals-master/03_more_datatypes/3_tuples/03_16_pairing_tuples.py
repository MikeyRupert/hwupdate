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
list_num = [1,3,434,4,3,4,2,3,2,]
g = sorted(list_num)
list_tup = []
for i in g:
    g.reverse().pop(i)
    list_tup.append(i)
    

print(list_tup)

