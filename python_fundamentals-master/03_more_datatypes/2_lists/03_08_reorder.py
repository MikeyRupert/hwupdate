'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1
'''
while True:
    try:
        example_input = []
        for i in range(1,11):
            user_input = int(input('Number ->'))
            example_input.append(user_input)  
            g=list(enumerate(example_input,1))
        print(f'{g[1]},{g[3]},{g[5]},{g[7]},{g[9]},{g[8]},{g[6]},{g[4]},{g[2]},{g[0]}')
    except ValueError as e:
        print('enter a number')
    except TypeError as e:
        print('enter a number')

# print(f'{g[1]},{g[0]}')
