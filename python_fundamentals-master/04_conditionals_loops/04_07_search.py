'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
while True:
    try:
        user_guess = int(input('Enter a number between 0 and 1,000,000,000-->'))
        finder_input = int(input('Enter number you think they entered\n\t-->'))
        guesses=0
        while not user_guess == finder_input:
            guesses += 1
            finder_input = int(input('\nEnter number you think they entered\n\t-->'))
            if finder_input == user_guess:
                print(f'Congrats you found the number they entered {finder_input}')
                if guesses<5:
                    print(f'you should think about going to vegas playa')
                    print(f'that only took you {guesses} guesses')
                else:
                    print(f'\texcept it took yaa {guesses} cheif.')
                break
    except ValueError as e:
        print('Now yaa know we cant be doing that chief.')
 

    

