'''
Compare Two Password Lists
Given:
    old_passwords = {"admin123", "guest123", "root123"}
    new_passwords = {"admin123", "newpass", "strongpass"}
Find:
Reused passwords 
New passwords 
'''

old_passwords = {"admin123", "guest123", "root123"}
new_passwords = {"admin123", "newpass", "strongpass"}

reused_pwd = old_passwords.intersection(new_passwords)
new_pwd = new_passwords.difference(old_passwords)

print(f"Reused passwords : {reused_pwd}")
print(f"New passwords : {new_pwd}")