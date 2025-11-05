''' 
Store login attempts in a list of tuples:
attempts = [("admin", "success"), ("guest", "failed"), ("root", "failed")]
Print only failed login users.
'''

attempts = [("admin", "success"), ("guest", "failed"), ("root", "failed")]

failed_attempts = [ attempt for attempt in attempts if attempt[1] == "failed"]

print(failed_attempts)


'''
If you want to print only the usernames of failed attempts
failed_users = [user for (user, status) in attempts if status == "failed"]
print(failed_users)
'''