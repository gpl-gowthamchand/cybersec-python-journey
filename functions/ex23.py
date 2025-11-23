'''
Count Secure vs Insecure Services
Given:
    services = {"SSH": 22, "HTTP": 80, "FTP": 21, "HTTPS": 443}
Write a function that counts how many are secure (22, 443) and insecure (21, 80).
'''

def count_services(services):
    secure_ports = {22, 443}
    insecure_ports = {21, 80}

    secure_count = 0
    insecure_count = 0

    for service, port in services.items():
        if port in secure_ports:
            secure_count += 1
        elif port in insecure_ports:
            insecure_count += 1

    return secure_count, insecure_count


services = {"SSH": 22, "HTTP": 80, "FTP": 21, "HTTPS": 443}

secure, insecure = count_services(services)
print("Secure services:", secure)
print("Insecure services:", insecure)
