'''
Write a simple aggregate function, sum(), that takes a list a returns the sum.

'''

n=[3,4,34,2,34,5,3,2,3,]
def sum_list(n):
    yield (sum(n))
print(next(sum_list(n)))
