'''
Count Word Occurrences
Write a function word_count(sentence) that returns a dictionary of each word’s count.
 
  "python is fun and python is powerful"

Output: {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}

'''

def word_count(sentence):
  word_count_dict = {}
  words = sentence.split()
  for word in words:
    if word in word_count_dict:
      word_count_dict[word] += 1
    else:
      word_count_dict[word] = 1

  return word_count_dict


sentence = "python is fun and python is powerful"
print(word_count(sentence))



''' shorter versiion 

from collections import Counter

def word_count(sentence):
    return dict(Counter(sentence.split()))

'''

