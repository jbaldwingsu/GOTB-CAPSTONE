from flask import Flask, render_template
import socket
import re

app = Flask(__name__)
logs = []

# implement log parsing
def parse_syslog_message(message):
    """
    Parse syslog messafe and extract relavent fields.
    """

    # regular expressoio to match syslog message format
    syslog_pattern = r'(?P<timestamp>^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s(?P<hostname>\S+)\s(?P<process>\S+):\s(?P<message>.*)$'
    
    match = re.match(syslog_pattern, message)
    if match:
        parsed_data = match.groupdict()
        return parsed_data
    
    else:
        return None


# script that listens for syslog messages
def syslog_server (host, port):
    # creating UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # bind the socket to a host and port
    server_socket.bind((host, port))

    print (f"Syslog server listening on {host} : {port}...")

    try: 
        while True:
            # recieve syslog messages
            message, address = server_socket.recvfrom(4096)
            print(f"Recieved message from {address}: {message.decode('utf-8')}")

            # append syslog message to logs lists
            logs.append(message.decode('utf-8'))

            parsed_data = parse_syslog_message(message.decode('utf-8'))
            if parsed_data:
                    print("Parsed syslog message:")
                    print(parsed_data)
            
            else:
                print("Failed to parse syslog message:")
                print(message.decode('utf-8'))


            # processing / forwarding logic -- add here 

    except KeyboardInterrupt:
        print("\nShutting down...")
        server_socket.close()

@app.route('/')
def index():
    return render_template('index.html', logs=logs)

if __name__ == "__main__":
    # def the host and port to listen on
    HOST = '0.0.0.0'    # all available network interfaces
    PORT = 514          # standard port for syslog

    import threading
    threading.Thread(target=syslog_server, args=(HOST, PORT), daemon=True).start()
    app.run(debug=True)

    # start syslog server
    syslog_server(HOST, PORT)