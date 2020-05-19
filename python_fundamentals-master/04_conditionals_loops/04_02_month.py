'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
def monty():
    try:
        months = ['January','February','March','April','May','June','July','August','September','October','November','December']
        Calender = dict(enumerate(months,start=1))
        user=int(input('Input Number between 1-12 to find corresponding month.\n-->'))
        while user<1 or user>=13 or user == str(user):
            user = int(input('figure it out bud, enter number between 1 and 12'))
        for k,v in Calender.items():
            if user== k:
                return f"{v} is the {user} month of the year."
    except ValueError as e:
        return 'Must enter a number between 1 and 12 to find that month'
        user= int(input('e'))
print(monty())
