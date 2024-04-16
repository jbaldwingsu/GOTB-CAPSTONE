# port_scanner.py

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
            # Uncomment the line below if you want to print error messages
            # print(f"Port {port} is closed or cannot be reached: {e}")
            pass
    return open_ports

if __name__ == "__main__":
    host = input("Enter the target host/IP address: ")
    ports = [int(port) for port in input("Enter the ports to scan (comma-separated): ").split(",")]

    open_ports = scan_ports(host, ports)
    print("Open ports:", open_ports)
