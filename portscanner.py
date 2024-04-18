# port_scanner.py

import sys
import socket

def scan_ports(host, ports):
    open_ports = []
    for port in ports:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)  # Set a timeout for connection attempt
                s.connect((host, port))
                open_ports.append(port)
        except Exception as e:
            pass
    return open_ports

if __name__ == "__main__":
    host = sys.argv[1]
    ports = [int(port) for port in sys.argv[2].split(",")]

    open_ports = scan_ports(host, ports)
    print("Open ports:", open_ports)
