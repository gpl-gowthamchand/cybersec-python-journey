'''
Login Attempt Tracker

Store login attempts:
 logins = [
    ("admin", "success"),
    ("guest", "failed"),
    ("root", "failed"),
    ("admin", "failed"),
 ]
Create a dictionary showing how many times each user failed to login:

 Output: {'guest': 1, 'root': 1, 'admin': 1}
(Hint: Loop through list and count using dict)

'''

logins = [
    ("admin", "success"),
    ("guest", "failed"),
    ("root", "failed"),
    ("admin", "failed"),
]

failed_attempts = {}

for username, status in logins:
    if status == "failed":
        if username in failed_attempts:
            failed_attempts[username] += 1
        else:
            failed_attempts[username] = 1

print(failed_attempts)


''' 
collections.Counter:

from collections import Counter

failed_attempts = Counter(user for user, status in logins if status == "failed")
print(dict(failed_attempts))
'''