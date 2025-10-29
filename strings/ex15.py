''' Split and join words

   Enter a sentence: i love python programming
   Original sentence: i love python programming
   Words after splitting: ['i', 'love', 'python', 'programming']
   Rejoined sentence: i-love-python-programming
'''

text = input("Enter a sentence: ")
Words = text.split()
rejoined = "-".join(Words)

print(f"Original sentence: {text}")
print(f"Words after splitting: {Words}")
print(f"Rejoined sentence: {rejoined}")