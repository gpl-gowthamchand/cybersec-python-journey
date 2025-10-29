# Count vowels and consonants 

s = input("Enter a string: ")
s = s.lower()
vowel_count = 0
consonant_count = 0 
vowels = ['a', 'e', 'i', 'o', 'u']
length = len(s)
print(f"total length of string: {length}")


i = 0
while i < length:
    if s[i].isalpha():  # only count letters
        if s[i] in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    i += 1


print(f"Total vowels : {vowel_count}")
print(f"Total consonants : {consonant_count}")