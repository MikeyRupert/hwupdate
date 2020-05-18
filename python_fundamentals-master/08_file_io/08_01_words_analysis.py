'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
def minime(txt):
    with open(txt, 'r') as bert:
              words = bert.read().split()
    min_q = len(min(words, key=len))
    return [word for word in words if len(word) == min_q]
print('\n')
print(','.join(minime('words.txt')))

def longfellow(txt):
    with open(txt, 'r') as bert:
              words = bert.read().split()
    max_q = len(max(words, key=len))
    return [word for word in words if len(word) == max_q]
print('\n')
print(', '.join(longfellow('words.txt')))

def total(txt):
    with open(txt, 'r') as bert:
              words = bert.read().split()
    len_q = len(words)
    return f'There are {len_q} objects ~ words in this words.txt file'
print('\n')
print(total('words.txt'))
print('\n')