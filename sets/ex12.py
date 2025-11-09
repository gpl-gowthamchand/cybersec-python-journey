'''
Blacklisted IP Detection
    active_ips = {"192.168.1.5", "10.0.0.8", "172.16.0.2"}
    blacklist = {"10.0.0.8", "8.8.8.8"}
Print all IPs that are blacklisted and active (intersection).'''

active_ips = {"192.168.1.5", "10.0.0.8", "172.16.0.2"}
blacklist = {"10.0.0.8", "8.8.8.8"}

print(f"ips that are blacklisted and active : {active_ips.intersection(blacklist)}")