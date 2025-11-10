## Returning Multiple Values - Python can return multiple values using a tuple.

def scan_ports():
    open_ports = [22, 80]
    closed_ports = [21, 25]
    return open_ports, closed_ports

open_p, closed_p = scan_ports()
print("Open:", open_p)
print("Closed:", closed_p)
