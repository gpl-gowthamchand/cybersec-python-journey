'''
Remove Duplicates from a Sentence
Input:  "python python is fun fun"
Convert it into a set of unique words.
'''

text = "python python is fun fun".split()
unique_words = set(text)
print(unique_words)

unique_sentence = " ".join(unique_words)
print(unique_sentence)