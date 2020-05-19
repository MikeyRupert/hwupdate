'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
'''wouldnt reccommend it'''
# while n in range(1,1001):
#    if n%5 == 0:
#        n +=1
# print(n)
print(list(i for i in range(0,1001,5)),end='  ')
