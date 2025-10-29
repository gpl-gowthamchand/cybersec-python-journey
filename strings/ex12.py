# Format a message dynamically (f-string)


marks = int(input("Enter your marks: "))
name = input("Enter your name: ")

print(f"{name}, you have {'passed' if marks >= 40 else 'failed'} the exam with {marks} marks.")
