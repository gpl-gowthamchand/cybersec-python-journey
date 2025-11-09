'''
Check if Any IP Sets Overlap
    internal_ips = {"192.168.1.1", "192.168.1.2"}
    external_ips = {"10.0.0.1", "8.8.8.8"}
Use .isdisjoint() to verify if they overlap(do they have common in both).
'''

internal_ips = {"192.168.1.1", "192.168.1.2"}
external_ips = {"10.0.0.1", "8.8.8.8"}

print(f"Do both ip sets overlaps each other: {internal_ips.isdisjoint(external_ips)}")


'''
Explanation
.isdisjoint() returns:
True -> if the two sets have no elements in common
False -> if they share at least one element
'''