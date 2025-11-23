'''
Extract IP Addresses
Write a function:
    def extract_ips(logs):
    Input example: ["User admin IP:192.168.1.5", "Guest IP:10.0.0.1"]
    Output: ["192.168.1.5", "10.0.0.1"]
'''

def extract_ips(logs):
    ips = []
    for log in logs:
        words = log.split()
        for word in words:
            if word.count(".") == 3:
                # Remove prefix before the IP
                ip = word.split(":")[-1]
                ips.append(ip)
    return ips

logs = ["User admin IP:192.168.1.5", "Guest IP:10.0.0.1"]
print(extract_ips(logs))