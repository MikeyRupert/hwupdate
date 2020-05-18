'''
Write a script that demonstrates a try/except/else.

'''
try:
    f=open('fido.txt')
    if f.name == 'fido.txt':
         raise Exception
except FileNotFoundError as p:
    print(p)
except Exception as p:
    print('all bad')
else:
    print(f.read())
    f.close()
finally:
    print('Runnn....')