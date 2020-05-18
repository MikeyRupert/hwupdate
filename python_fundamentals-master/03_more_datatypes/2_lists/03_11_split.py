'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
def word_count(str):
	counts = dict()
	words = str.split()
	for word in words:
	    if word in counts:
	        counts[word] += 1
	    else:
	        counts[word] = 1
	return counts
print(word_count('hey hey you'))
