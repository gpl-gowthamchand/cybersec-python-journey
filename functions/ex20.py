'''
Compare Two IP Lists (Safe vs Blacklisted)
    safe_ips = {"192.168.1.5", "10.0.0.1", "172.16.0.2"}
    blacklist = {"10.0.0.1", "8.8.8.8"}
Write a function check_blacklisted(safe, black)
Returns IPs that are in both sets (intersection).
'''


def check_blacklisted(safe, black):
    return safe.intersection(black)

safe_ips = {"192.168.1.5", "10.0.0.1", "172.16.0.2"}
blacklist = {"10.0.0.1", "8.8.8.8"}

print(check_blacklisted(safe_ips, blacklist))