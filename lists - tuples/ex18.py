''' 
Combine two lists:

One of usernames → ["admin", "guest", "root"]

One of passwords → ["1234", "guest123", "rootpass"]

Make a list of tuples: [("admin", "1234"), ("guest", "guest123"), ...] '''


usernames = ["admin", "guest", "root"]
passwords = ["1234", "guest123", "rootpass"]

userCredentials = [(username, password) for username, password in zip(usernames, passwords)]

print(userCredentials)


# userCredentials = list(zip(usernames, passwords))
