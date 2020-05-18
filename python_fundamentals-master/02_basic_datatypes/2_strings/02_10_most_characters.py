'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
scrip = []
for i in range(3):
    user_input = input('String\n\t-->')
    scrip.append(user_input)
    for word in scrip:
        print(f'{len(word)}, {word}')
    

    

    
    
    
    