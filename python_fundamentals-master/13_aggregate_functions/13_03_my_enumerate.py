'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''
grocery = ['pickles','buns','meat','lettice','chips','soda']
def my_enumerate():
      for i,num in enumerate(grocery):
            yield i,num
g= list(my_enumerate())
for i in g:
      print(i,end='\n')
