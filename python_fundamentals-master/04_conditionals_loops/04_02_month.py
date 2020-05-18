'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
months = ['\tJanuary','\tFebruary','\tMarch','\tApril','May','\tJune','July','\tAugust','\tSeptember','\tOctober','\tNovember','\tDecember']
user_input=int(input('Input Number between 1-12 to find corresponding month.\n-->'))

for num,month in list(enumerate(months, start=1)):
    if user_input == num:
        print(month)
    else:
        print("Other")
            


