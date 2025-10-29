''' Remove special characters from a string 


Enter a string with special chars: Hap@p!y# Co$$ding!!
The cleaned string is : HappyCoding
'''

s = input ("Enter a string with special chars: ")

s_cleaned = []

length = len(s)

i = 0
while (i < length):
    if s[i].isalpha():
        s_cleaned.append(s[i])
    i = i+1

cleaned_string = "".join(s_cleaned)        

print(f"The cleaned string is : {cleaned_string}")