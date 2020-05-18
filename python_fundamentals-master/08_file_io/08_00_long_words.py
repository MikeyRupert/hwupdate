'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
text = []
vent = []
with open('words.txt','r') as bong:
    for wordss in bong.readlines():
        wordss = wordss.strip()
        text += wordss

with open('words.txt') as blitz:
  for line in blitz:
    if len(line.strip()) > 19:
      vent.append(line)
      print(line)


with open('hamiltons.txt', 'w') as venti:
  venti.write('\n'.join(vent))
