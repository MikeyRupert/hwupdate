'''
Fahrenheit to Celsius:

Write the necessary code to read a degree in Fahrenheit from the console
then convert it to Celsius and print it to the console.

    C = (F - 32) * (5 / 9)

Output should read like - "81.32 degrees fahrenheit = 27.4 degrees celsius"


'''
def temp():
    current_temp = float(input('degree fahreheit\t->'))
    cel = format((current_temp-32)*(5/9),'1.2f')
    print(f'\n\t{current_temp} degrees fahrenheit = {float(cel)} degrees celsius\n')
temp()