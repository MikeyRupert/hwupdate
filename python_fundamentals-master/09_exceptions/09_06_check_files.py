'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
calc = []
mult = []
try:
    with open('integers.txt', 'r') as r:
        numbers = r.readlines()
        for n in numbers:
            n=int(n)
            calc.append(n)
except Exception as e:
    print(e)
except ValueError:
    print('well this is really helpful')
except IOError as e:
    print(e)
finally:
    for number in range(len(calc)):
        w = number*20
        mult.append(w)
    print(f'\tevery number in intergets.txt is multiplied by 20\n\t\told list not pretty-->{numbers}\n\t\t\tpeep it out-->{mult}')
    


