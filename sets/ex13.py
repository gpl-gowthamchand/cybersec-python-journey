'''
Safe IP Filtering
print all active IPs that are not blacklisted.
    active_ips = {"192.168.1.5", "10.0.0.8", "172.16.0.2"}
    blacklist = {"10.0.0.8", "8.8.8.8"}
'''

active_ips = {"192.168.1.5", "10.0.0.8", "172.16.0.2"}
blacklist = {"10.0.0.8", "8.8.8.8"}

print(f"safe ips : {active_ips.difference(blacklist)}")


## difference [ - or .difference() ] - keeps items that are in one set but not both 
