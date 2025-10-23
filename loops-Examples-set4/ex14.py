#Count how many vowels are present in an input string.

string = input("Enter a string: ")
length = len(string)
vowels_set = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U" ]
count = 0

for i in range (length):
    if string[i] in vowels_set:
        count = count+1

print(f"Number of vowels in {string} : {count}")


'''
string = input("Enter a string: ")
vowels = set("aeiouAEIOU")
count = sum(1 for ch in string if ch in vowels)
print(f"Number of vowels in {string} : {count}")
'''