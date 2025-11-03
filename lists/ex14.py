# Count the number of failed login attempts.

attempts = [("admin", "success"), ("guest", "failed"), ("root", "failed")]

count = 0 

for attempt in attempts:
    if attempt[1] == "failed":
        count += 1 

print(f"No of failed attempts: {count}")
