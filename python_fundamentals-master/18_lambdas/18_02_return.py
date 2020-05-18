'''
Write a lambda function that does not take in an arguments but returns a value.
Print the return value.

'''
age = [2, 6, 8, 10,70, 50, 11, 4, 12, 80, 7, 13, 17, 0, 3,33, 21]
oldenough = list(filter(lambda num: (num > 18), age))
print(oldenough)