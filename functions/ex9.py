'''
Count Vowels in a String
Write a function count_vowels(s) that returns the number of vowels in a given string.
'''

def count_vowels(s):
    count = 0
    s = s.lower()
    for ch in s:
        if ch in "aeiou":
            count += 1
    return count


s = "Apple"
print(count_vowels(s))


''' shortest way 

def count_vowel(s):
    return sum(1 for ch in s.lower() if ch in "aeiou" )

'''