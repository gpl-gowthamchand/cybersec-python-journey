''' Filter blacklisted IPs:
ips = ["192.168.1.5", "10.0.0.8", "172.16.0.2"]
blacklist = ["10.0.0.8"]
# Output: only IPs not in blacklist
'''

ips = ["192.168.1.5", "10.0.0.8", "172.16.0.2"]
blacklist = ["10.0.0.8"]
filtered_ips = []

for ip in ips:
    if ip not in blacklist:
        filtered_ips.append(ip)


print(f"Filtered ips : {filtered_ips}")


''' using a list comprehension

filtered_ips = [ip for ip in ips if ip not in blacklist]

'''