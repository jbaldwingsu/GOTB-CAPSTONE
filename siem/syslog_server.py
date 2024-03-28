from flask import Flask, render_template, request
import socket
import re
import sqlite3
import mysql.connector
import random
app = Flask(__name__, template_folder='templates')
# function to fetch logs from SQLite DB 
# (COMMENT OUT EVERYTHING FROM UNDER TRY > ABOVE RETURN LOGS)

# Function to create the 'siem' database if it doesn't exist
def create_database():
    try:
        # Connect to MySQL server without specifying a database
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="thunderbear"
        )

        cursor = db_connection.cursor()

        # Create the 'siem' database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS siem")

    except mysql.connector.Error as e:
        print("Error:", e)

    finally:
        if 'db_connection' in locals() or 'db_connection' in globals():
            db_connection.close()

# Call the function to create the 'siem' database
create_database()

def get_logs_from_db():
    try:
        # Connect to the MySQL database
        dataBase = mysql.connector.connect(
            host="localhost",
            user="root",
            password="thunderbear",
            database="siem"
        )
        cursorObject = dataBase.cursor()

        # Create the network_logs table if it doesn't exist
        cursorObject.execute("""
            CREATE TABLE IF NOT EXISTS siem (
                timestamp DATETIME,
                source_ip VARCHAR(255),
                destination_ip VARCHAR(255),
                protocol VARCHAR(255),
                message TEXT
            )
        """)
        
        # mock logs to test
        # mock_logs = []
        # for i in range(5):
        #     timestamp = "2024-03-03 12:00:00"
        #     source_ip = f"192.168.{i+1}.100"
        #     destination_ip = f"8.{i+1}.8.8"
        #     protocol = f"Protocol Template {i+1}"
        #     message = f"Message {i+1}"

        #     cursorObject.execute("INSERT INTO siem (timestamp, source_ip, destination_ip, protocol, message) VALUES (%s, %s, %s, %s, %s)",
        #                         (timestamp, source_ip, destination_ip, protocol, message))
        #     dataBase.commit()
        #     mock_logs.append({"timestamp": timestamp, "source_ip": source_ip, "destination_ip": destination_ip, "protocol": protocol, "message": message})

        # Fetch logs from the database
        cursorObject.execute("SELECT * FROM siem")
        rows = cursorObject.fetchall()

        # Convert fetched logs from tuples to dictionaries
        keys = ['timestamp', 'source_ip', 'destination_ip', 'protocol', 'message']
        logs = [dict(zip(keys, row)) for row in rows]

        return logs

    except mysql.connector.Error as e:
        print("Error:", e)
        return []
    finally:
        if 'dataBase' in locals() or 'dataBase' in globals():
            dataBase.close()

app = Flask(__name__)             
app = Flask(__name__, template_folder='templates') 
logs = []

# generate dummy logs for demo (USE TO SEE CORRECT VISUAL)
    # (start, n+1 end)
# for i in range (1,101):
#     logs.append({"timestamp": f"2024-03-03 12:00:0{i-1}", "source_ip": f"192.168.{i}.100", "destination_ip": f"8.{i}.8.8", "protocol": f"Protocol Template {i}", "message" : f"Message {i}"})


# implement log parsing (non-functional)
def parse_syslog_message(message):
    """
    Parse syslog messafe and extract relavent fields.
    """

    # regular expression to match syslog message format (LINKED WITH FOR LOOP DISPLAYING MOCK LOGS)
    syslog_pattern = r'(?P<timestamp>^\w{3}\s+\d{1,2}\s+\d{2}:\d{2}:\d{2})\s(?P<source_ip>\S+)\s(?P<destination_ip>\S+)\s(?P<protocol>\S+):\s(?P<message>.*)$'
    
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
    
    # bind the socket to a host and port (NOT NEEDED)
    # server_socket.bind((host, port))

    print (f"Syslog server listening on {host} : {port}...")

    try: 
        while True:
            # recieve syslog messages
            message, address = server_socket.recvfrom(4096)
            print(f"Recieved message from {address}: {message.decode('utf-8')}")

            parsed_data = parse_syslog_message(message.decode('utf-8'))
            if parsed_data:
                print("Parsed syslog message:")
                print(parsed_data)
                    
                try:
                    # connect to the mysql database
                    dataBase = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="thunderbear",
                        database="siem"
                    )
                    cursorObject = dataBase.cursor()

                    # insert parsed data into the siem table
                    cursorObject.execute("""
                        INSERT INTO siem (timestamp, source_ip, destination_ip, protocol, message)
                        VALUES (%s, %s, %s, %s, %s)
                    """, (parsed_data['timestamp'], parsed_data['source_ip'], parsed_data['destination_ip'], parsed_data['protocol'], parsed_data['message']))
                    dataBase.commit()

                except mysql.ConnectionError as e:
                    print("Error:", e)
                
                finally: 
                    if 'dataBase' in locals() or 'dataBase' in globals():
                        dataBase.close()

            else:
                print("Failed to parse syslog message:")
                print(message.decode('utf-8'))

            # processing / forwarding logic -- add here 

    except KeyboardInterrupt:
        print("\nShutting down...")
        server_socket.close()

@app.route('/')
def index():
   
    # logs fetch from db
    logs = get_logs_from_db()
    
    # pagination structure 
    page = request.args.get('page', 1, type=int)
    per_page = 20
    total_logs = len(logs)
    total_pages = total_logs // per_page + (total_logs % per_page > 0)
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_logs = logs[start_idx:end_idx]

    # search action
    search_term = request.args.get('search', '')
    if search_term:
        paginated_logs = [log for log in logs if search_term.lower() in log['message'].lower()]

    return render_template('index.html', logs=paginated_logs, page=page, total_pages=total_pages)


if __name__ == "__main__":
    # def the host and port to listen on
    HOST = '0.0.0.0'    # all available network interfaces
    PORT = 514          # standard port for syslog

    import threading
    threading.Thread(target=syslog_server, args=(HOST, PORT), daemon=True).start()
    app.run(debug=True)

    # start syslog server
    # syslog_server(HOST, PORT)