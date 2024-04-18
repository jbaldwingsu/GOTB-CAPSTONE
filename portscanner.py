# port_scanner.py

import sys
import socket
import json

def scan_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)  # Set a timeout for connection attempt
            s.connect((host, port))
            return True
    except Exception as e:
        return False

def scan_ports(host, ports):
    open_ports = []
    closed_ports = []
    for port in ports:
        if scan_port(host, port):
            open_ports.append(port)
        else:
            closed_ports.append(port)
    return open_ports, closed_ports

if __name__ == "__main__":
    host = sys.argv[1]
    ports = [int(port) for port in sys.argv[2].split(",")]

    open_ports, closed_ports = scan_ports(host, ports)

    # Create a dictionary to represent the scanning results
    result = {
        "Open Ports": open_ports,
        "Closed Ports": closed_ports
    }

    # Convert the dictionary to JSON format
    json_result = json.dumps(result)

    # Print the JSON result
    print(json_result)
