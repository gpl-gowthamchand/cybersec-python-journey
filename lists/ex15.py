''' Extract all domains from a list of emails:
emails = ["user1@gmail.com", "admin@yahoo.com", "tester@outlook.com"]
Output: ['gmail.com', 'yahoo.com', 'outlook.com']
'''

emails = ["user1@gmail.com", "admin@yahoo.com", "tester@outlook.com"]

usernames = []
domains = []



for email in emails:
    username, domain = email.split("@")
    usernames.append(username)
    domains.append(domain)

print(domains)