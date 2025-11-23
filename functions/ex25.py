'''
Check Suspicious Login Activity
Write a function:
    def detect_suspicious(logs, user):
Input:
    logs = {"admin": 5, "root": 10, "guest": 1}
If the login count for user > 5 → print “Suspicious Activity Detected”.
'''

def detect_suspicious(logs, user):
    if logs.get(user, 0) > 5:
        print("Suspicious Activity Detected")
    else:
        print("No Suspicious Activity")

logs = {"admin": 5, "root": 10, "guest": 1}

detect_suspicious(logs, "admin")  
detect_suspicious(logs, "root") 
detect_suspicious(logs, "guest")  
