'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
# '''
text = []
rev_list = []
rr=[]

for line in (list(open("words.txt"))):
    text.append(line[::-1].strip())
for word in text:
    rev_list.append(word)


with open('words_reverse.txt', 'w') as backwards:
    backwards.write('\n'.join(rev_list))

with open('words_reverse.txt', 'r') as r:
    for word in r.readlines():
        word =word.rstrip()
        rr.append(word)
print('\n'.join(rr))