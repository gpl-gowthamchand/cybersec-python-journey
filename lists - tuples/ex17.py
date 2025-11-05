''' 
Create a tuple of ports (80, 22, 443, 21)
Check if port 22 exists in it (used for SSH).
'''

ports = (80, 22, 443, 21)

if 22 in ports:
    print("Port 22 found - used for SSH")
else :
    print("Port 22 not found")