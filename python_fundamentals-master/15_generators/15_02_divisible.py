'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
def div1111():
    for i in range(1000000):
         if i%1111==0:
             yield i
d11 = div1111()   
print(next(d11))
print(next(d11))
print(next(d11))
print(next(d11))
print(next(d11))
list_ = [i for i in range(10000000)]
created_generator = (i for i in ([i for i in range(1000000)]) if i%1111==0)
print(next(created_generator))
print(next(created_generator))
print(next(created_generator))
print(list(created_generator))
