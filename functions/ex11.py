'''Check for Palindrome
Write a function is_palindrome(word) that returns True if the word reads the same backward.'''

def is_palindrome(word):
    word = word.lower()
    reversed_word = word[::-1]
    if reversed_word == word:
        return True
    else:
        return False

print(is_palindrome("Mom"))


