'''
Input marks of a student and print grade:
Marks ≥ 90 → A
Marks ≥ 80 → B
Marks ≥ 70 → C
Else → Fail
'''

marks = int(input("Enter your marks: "))

if (marks >= 90):
    print("A")

elif (marks >= 80):
    print("B")

elif (marks >= 70):
    print("C")

else:
    print("Fail")