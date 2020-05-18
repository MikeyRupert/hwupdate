'''
Using a "for-loop", print out all odd numbers from 1-100.

'''
odd = [i for i in range(1,101) if not i%2==0]
print('\t\tyo odd list\n\n',odd)
# for i in range(1,101):
#     if not i%2==0:
#         print(i, end=',')

