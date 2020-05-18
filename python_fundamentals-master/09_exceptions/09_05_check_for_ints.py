'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
while True:
    try:
        age = int(input('What... is the air-speed velocity of an unladen swallow?\n\t-->'))
        if age<26 and age >= 24: 
            print('Right. Off you go.')
            print("average cruising airspeed velocity of an unladen European Swallow is roughly 11 meters per second, or around 24 miles an hour")
            break
        elif age < 24:
            print('too low peasent')
            print('Next')
        elif age > 26:
            print('too high peasent')
            print('Goodbye')
            print('Next')
        # else:
            # pass
    except ValueError:
        print("I don't know that! Auuuuuuuugh!")
    else:
        print("Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.")
    finally:
        print('What... is your quest?')
