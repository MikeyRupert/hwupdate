'''
In this exercise, you will practice both File I/O as well as using Exceptions
in a real-world scenario.

You have a folder containing three text files of books from Project Gutenberg:
- war_and_peace.txt
- pride_and_prejudice.txt
- crime_and_punishment.txt

1) Open war_and_peace.txt, read the whole file content and store it in a variable

2) Open crime_and_punishment.txt and overwrite the whole content with an empty string

3) Loop over all three files and print out only the first character each. Your program
    should NEVER terminate with a Traceback.

    a) Which Exception can you expect to encounter? Why?
file or directory nott found
    b) How do you catch it to avoid the program from terminating with a Traceback?
try, except

BONUS CHALLENGE: write a custom Exception that inherits from Exception and raise it if the
first 100 characters of any of the files contain the string "Prince".

'''

# with open('war_and_peace.txt', 'r') as f:
#     f = (f.read())
# with open('crime_and_punishment.txt','w+') as w:
#     w.write('')
#     w.seek(0)
#     w = w.read()
#     # print(w)
# class PurpleRain(Exception):
#     pass

# try:
#     with open('war_and_peace.txt','r') as a, open('crime_and_punishment copy.txt','r') as b, open('pride_and_prejudice.txt','r') as c:
#         a1 = a.readlines(100)
#         b1 = b.readlines(100)
#         c1 = c.readlines(100)
#         for i in a1,b1,c1:
#             print(i[1])
#            words= []
#            words.append(i)
#            for word in words.strip():
#                print(word)
               
# except Exception:
#     raise p('tt')

with open('war_and_peace.txt','r') as a, open('crime_and_punishment copy.txt','r') as b, open('pride_and_prejudice.txt','r') as c:
    a1 = a.readline()
    b1 = b.readline()
    c1 = c.readline()
    for i in a1.split(),b1.split(),c1.split():
        print(i[1])
        
               
    
    
                # if 'Prine' in i:
                    # raise PurpleRain
    # except IOError as PurpleRain:
        # raise PurpleRain('charlie murphy')
                