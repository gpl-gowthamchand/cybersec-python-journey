''' Find and replace words

   Enter a sentence: i love kotlin programming
   Enter a word to find: kotlin
   Enter a word to replace: python 
   The original sentence: i love kotlin programming
   The modified sentence: i love python programming
'''

text = input("Enter a sentence: ")
wordToFind = input("Enter a word to find: ")
wordToReplace = input("Enter a word to replace: ")

print(f"The original sentence: {text}")

text = text.replace(wordToFind, wordToReplace)

print(f"The modified sentence: {text}")