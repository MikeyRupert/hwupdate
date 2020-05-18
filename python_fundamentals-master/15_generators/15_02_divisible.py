'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
list_ = [i for i in range(10000000)]
created_generator = (i for i in (list_) if i%1111==0)
print(list(created_generator))
