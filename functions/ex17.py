'''
Count Failed Login Attempts
Given a list: logins = [("admin", "failed"), ("root", "failed"), ("guest", "success")]
Write a function count_failed(logins) that returns how many users failed to log in.
'''

def count_failed(logins):
    count = 0
    for login in logins:
        user, attempt = login
        if attempt == "failed":
            count += 1

    return count


logins = logins = [("admin", "failed"), ("root", "failed"), ("guest", "success")]
print(count_failed(logins))


'''Shorter version:
def count_failed(logins):
    return sum(1 for _, attempt in logins if attempt == "failed")

'''