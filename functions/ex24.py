'''
Find Reused Passwords
Write a function find_reused(old, new) that takes two sets of passwords and returns reused ones.
'''

def find_reused(old, new):
    return old.intersection(new)

old = {"admin123", "guest123", "root123"}
new = {"admin123", "newpass", "strongpass"}

print(find_reused(old, new))
