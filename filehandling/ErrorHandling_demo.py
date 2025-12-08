try:
    # 1. ATTEMPT
    # This block executes first. If the file exists, it opens it, reads it, and prints the content.
    with open("demo.txt", "r") as file:
        print("file exists, the content inside is : \n")
        print(file.read())

# 2. FILE NOT FOUND HANDLER
# If the file open fails specifically because the file doesn't exist, control jumps here.
except FileNotFoundError:
    print("the file is not existing, check once")

# 3. GENERIC HANDLER
# If any other error happens (e.g., PermissionError, encoding error, etc.), control jumps here.
except Exception as e:
    print(f"an unknown error occured: {e}")