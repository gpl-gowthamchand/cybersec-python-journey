'''
Port Classification
Write a function:  def check_port(port):
If port = 22 or 443 → return "Secure"
If port = 21 or 23 → return "Insecure"
Else → "Unknown"
'''

def check_port(port):

    secure_ports =[22, 443]
    insecure_ports = [21, 23]

    if port in secure_ports:
        return "Secure"
    elif port in insecure_ports:
        return "Insecure"
    else:
        return "Unknown"



print(check_port(23))
