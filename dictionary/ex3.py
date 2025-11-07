'''
Input: "python is fun and python is powerful"
Output: {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}
(Hint: split the string, then use a dictionary to count)
'''

s = "python is fun and python is powerful"
words = s.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)


''' 
Shortcut (using collections.Counter)
Python also has a built-in way to do this easily:

from collections import Counter
s = "python is fun and python is powerful"
word_count = Counter(s.split())
print(word_count)

'''