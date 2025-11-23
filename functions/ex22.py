'''
Email Domain Extractor
Write a function: 
    def extract_domain(email):
Input: "user@example.com"
Output: "example.com"
'''

def extract_domain(email):
    name, domain = email.split("@")
    return domain

email = "xyz@yahoo.com"
print(extract_domain(email))


'''Shorter version:
def extract_domain(email):
    return email.split("@")[-1]
'''