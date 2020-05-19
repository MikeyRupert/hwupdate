'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?
all the numbers up to the numbers we call a floor division by...1111
makes since becase there wouldnt be 
'''
# list_ = [i for i in range(10000000)]
created_generator = (i for i in ([i for i in range(10000000)]) if i//1111==0)
print((next(created_generator)))
print((next(created_generator)))
print((next(created_generator)))
print((next(created_generator)))
print((list(created_generator)))
print(created_generator)
print((str(created_generator)))