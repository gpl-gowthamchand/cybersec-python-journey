'''
Port Scanner Simulation
Create a function scan_ports(ports) that:

Takes a list of port numbers

Returns two lists: secure (22, 443) and insecure (21, 23, 25)
'''

def scan_ports(ports):
    secure_ports = [22, 443]
    insecure_ports = [21, 23, 25]

    secure = []
    insecure = []

    for port in ports:
        if port in secure_ports:
            secure.append(port)
        elif port in insecure_ports:
            insecure.append(port)

    return secure, insecure


ports_to_scan = [21, 22, 80, 443, 25, 23, 8080]
secure, insecure = scan_ports(ports_to_scan)

print("Secure Ports:", secure)
print("Insecure Ports:", insecure)
