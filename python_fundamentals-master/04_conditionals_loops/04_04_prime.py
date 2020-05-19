'''
Print out every prime number between 1 and 100.

'''
def primes():
    x = int(input('Enter a number\n\nWill print out all prime numbers\n\nEnter here-->'))
    for num in range(1,x):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(f' {num}, ',end='')
# primes()
print('Zee prime list',primes())

# def fib(n):
#     a,b = 0,1
#     while b<n:
#         print(b)
#         a,b=b,a+b
# a = fib(1000)
# og = list(a)-list(g)