## membership operatiion in strings 
text = "Python is fun"
print("Python" in text) 
print("Java" in text)
print("CPP" not in text)
print()


## equality and inequality comparision 
text1 = "apple"
text2 = "grapes"
print(text1 == text2)
print(text != text2)
print()

## lexicographical or alphabetical comparison 
s1 = "grapes"
s2 = "mango"
s3 = "Grapes"
print(s1 < s2) # g comes before m 
print(s1 > s3) # lowercase g has higher unicode than uppercase G 
print()

#Iterating through a string 
for i in "Python programming":
    print(i)