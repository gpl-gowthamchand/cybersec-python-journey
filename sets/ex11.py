'''
Unique IP Addresses
Given:
    ips = ["192.168.1.5", "192.168.1.5", "10.0.0.8", "172.16.0.2", "10.0.0.8"]
Find all unique IP addresses using a set.
'''

ips = ["192.168.1.5", "192.168.1.5", "10.0.0.8", "172.16.0.2", "10.0.0.8"]
unique_ips = set(ips)
print(f"Unique ips: {unique_ips}")


'''
Explanation:
Lists can have duplicates.
Converting to a set automatically keeps only unique elements.
'''