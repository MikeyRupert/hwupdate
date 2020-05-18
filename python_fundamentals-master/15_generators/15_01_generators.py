'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.
'''

'''typical function'''
# def func():
#     for n in range(2,6):
#         print(n)

'''typical generator, difference is yield symbol'''
# def generator():
#     for n in range(2,6):
#         yield(n)
# # func()
# # prints the basics listcl
# # print(type(func()))
# print(type(generator()))
# generator()
# using_generator = generator()
# # next(using_generator()) dont call this or its all bad
# print(next(using_generator))
# print(next(using_generator))
# print(next(using_generator))
# print(next(using_generator))
# # print(next(using_generator)) will produce stopiteration
# using_generator = generator()
# print(next(using_generator))
# print(type(next(using_generator)))

'''generator in oneliner'''
generator_object = (i for i in range(1,10000,6) if i in range(3,1000,5))
print('\n')
print("this is what it looks like on the outside")
print(generator_object)
print('\ncalling single generator object')
print('seeing the generator true colors.')
print(next(generator_object))
print('\nayyy look at this alot better.. getting somewhere',next(generator_object))
print(f'...inside a fstring {next(generator_object)}')
print('\n')
'''Ain't Nobody Got Time for That, use this'''
print('how to iterate over geneator object to see what it prints out')
for thing_to_iterate_generator in generator_object:
    print(thing_to_iterate_generator)


#     print('\n')
#     print('\n winner winner chicken dinner')
#     print(f'seeing the generator true colors...inside {thing_to_iterate_generator}')
 
    

