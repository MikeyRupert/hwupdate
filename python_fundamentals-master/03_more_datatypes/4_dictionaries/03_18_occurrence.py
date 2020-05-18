'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1

'''
gerneric_sentence = (input('write a sentect to find the occurance of each letter\n\t-->'))
word_count = {}
for common_words in gerneric_sentence:
    word_count[common_words] = word_count.get(common_words,0)+1
print(word_count) 
    