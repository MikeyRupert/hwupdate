'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''
print([(','.join(word for word in ('blowfish', 'clownfish', 'catfish', 'octopus') if word[-4:]=='fish'))])
