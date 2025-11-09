'''
Find Common Open Ports
Two scans report open ports:
    scan1 = {21, 22, 80, 443}
    scan2 = {22, 25, 443, 8080}
Find:
Common open ports
Ports newly found in scan2
'''

scan1 = {21, 22, 80, 443}
scan2 = {22, 25, 443, 8080}

print(f"Common open ports: {scan1.intersection(scan2)}")
print(f"New ports scanned in scan2: {scan2.difference(scan1)}")