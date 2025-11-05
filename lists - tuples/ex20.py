''' 
Extract all IP addresses from a list of strings:
logs = ["Access from 192.168.1.5", "Ping 10.0.0.8 failed", "Connected to 172.16.0.2"]
Expected: ['192.168.1.5', '10.0.0.8', '172.16.0.2']
'''

logs = [
    "Access from 192.168.1.5",
    "Ping 10.0.0.8 failed",
    "Connected to 172.16.0.2"
]

ips = []

for log in logs :
    words = log.split()
    for word in words:
        if word.count(".") == 3 : # ips has 3 dots
            ips.append(word)


print(ips)

