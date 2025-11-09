'''
Compare Two Log Files
    day1_logins = {"admin", "root", "guest"}
    day2_logins = {"admin", "guest", "hacker"}
Find:
Who logged in both days
Who logged in only on day 2
'''

day1_logins = {"admin", "root", "guest"}
day2_logins = {"admin", "guest", "hacker"}

print(f"logins on both days: {day1_logins.intersection(day2_logins)}")
print(f"logged only on day 2: {day2_logins.difference(day1_logins)}")