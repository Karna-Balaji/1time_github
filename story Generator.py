# The task is to generate a random story every time user runs the program.
# Every time the user runs the program, we must produce a random tale. We'll first store the
# portions of the tales in distinct lists, and then use the Random module to choose random
# sections of the stories from those lists

# Importing random Module
import random 

#Defining list of Phrases that helps tp build a story
a = ['About 1000 years ago, ', ' In the 100 BC, ', 'Once upon a time, ']
b = [' there lived a king. ', ' there was a thief named William Turner. ', ' there lived a farmer. ', 'there lived a pirate named Jack Sparrow. ']
c = [' One day ', ' One full-moon night ']
d= [' he was passing by ', ' he was going for a walk in ','he was going for an adventure ']
e = [' the mountains ', ' the garden ', 'an Island ']
f = [' he saw a man ', ' he saw a solider ']
g = [' who seemed to be old ', ' who seemed young ']
h = [' searching for Gold. ', ' digging for gold. ','searching for a rare treasure ']
i = ['The king ','The thief ','The Farmer ',' The Pirate ']
j = ['wanted to kill ','wanted to steal the loot from ','wanted to help and get equal shares for helping ']
k = ['The man ','The Young Lady ','The Pirate ']
L = ['But ','And ']
m = ['He Killed ','He stole from ',' He Helped ']
n = ['him ']
o = ['to get The rare treasure ','to get the Gold ']
p = ['and ']
q = ['went on their ways ','escaped from there ']

#selecting an item from each list using random.choice() and concatenating them to form a story
print(random.choice(a) + random.choice(b) +random.choice(c) + random.choice(d) + random.choice(e) + random.choice(f)
      +random.choice(g) + random.choice(h)+random.choice(i) +random.choice(j) + random.choice(k)  + random.choice(L)
+random.choice(m) + random.choice(n)+random.choice(o) +random.choice(p) + random.choice(q))

print()
print()
print("The End")
