'''
Write a script that generates an exception. Handle this exception with a try/except.
For example:

list_ = ["hello world!"]
print(list_[1])

This raises and exception that needs to be handled.

'''
while True:
        try:
            num1 = int(input("input a num\n\t-->"))
            num2 = int(input('input a num\n\t-->'))
            print(f'quotient: {num1*num2}')
        except ValueError:
            print('need a string mate')
# try:
#     list_ = ["hello world!"]
#     print(list_[1])
# except IndexError:
#     print('only one item in that list cheif, try chaning 1 to 0')
