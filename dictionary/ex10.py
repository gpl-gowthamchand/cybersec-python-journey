'''
Port Analysis

Given a dictionary of open ports:
  ports = {21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP", 443: "HTTPS"}

Print only insecure services (FTP, Telnet).
Print all secure ports (SSH, HTTPS).
Hint: use a loop with an if condition on value.
'''

ports = {21: "FTP", 22: "SSH", 23: "Telnet", 80: "HTTP", 443: "HTTPS"}
insecure = ["FTP", "Telnet"]
secure = ["SSH", "HTTP"]
for port, service in ports.items():
    if service in insecure:
        print(f"Insecure servies : {port} - {service}")

for port, service in ports.items():
    if service in secure:
        print(f"Secure servies : {port} - {service}")
