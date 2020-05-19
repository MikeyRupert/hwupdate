'''
Using list comprehension, create a list "positive" from the list
"numbers" that contains only the positive numbers from the list "numbers".

'''
'''build legos'''
# numbers = [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42]
# postive = [x for x in numbers if x%2==0 and not x<0]
# print('Gotta Stay Positive',sorted(postive))
'''build castle'''
print('Gotta Stay Positive',sorted([x for x in [5, -8, 3, 10, -19, -22, 44, 2, -1, 4, 42] if x%2==0 and not x<0]))
'''stay positive... u now have castle'''