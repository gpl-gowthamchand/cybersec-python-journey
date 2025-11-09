'''
Common Students
Given two sets of student names:
   python_students = {"Gowtham", "Arjun", "Neha"}
   java_students = {"Neha", "Kiran", "Arjun"}
Find students who are enrolled in both courses.
'''


python_students = {"Gowtham", "Arjun", "Neha"}
java_students = {"Neha", "Kiran", "Arjun"}

print(f"Common students in both the courses{python_students.intersection(java_students)}")


# intersection - common in both sets


''' alternative way 

common = python_students & java_students
print(f"Common students: {common}")
'''