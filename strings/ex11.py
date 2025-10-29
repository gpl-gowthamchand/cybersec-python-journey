# Extract domain from an email 

email = input("Enter email address: ")

if "@" in email and email.count("@") == 1:
    username, domain = email.split("@")
    print(f"Full Email: {email}")
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email address.")
