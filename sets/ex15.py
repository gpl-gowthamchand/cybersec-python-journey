'''
Detect New Threats
You have known malware signatures:
    known_signatures = {"Trojan", "Worm", "Adware"}
    new_scan = {"Trojan", "Spyware", "Ransomware"}
Find:
Threats already known
New threats detected
'''

known_signatures = {"Trojan", "Worm", "Adware"}
new_scan = {"Trojan", "Spyware", "Ransomware"}

print(f"Threats already known: {known_signatures.intersection(new_scan)}")
print(f"New threats: {new_scan.difference(known_signatures)}")