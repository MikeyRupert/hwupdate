'''
Print out every prime number between 1 and 100.

'''
# for num in range(1,101):
#     for i in num:
#         if 
#         # Program to check if a number is prime or not
def is_prime(n):
    status = True
    if n < 2:
        status = False
    else:
        for i in range(2,n):
            if n % i == 0:
                status = False
    return status
print(is_prime(100))