# heatmapcapture.py
import time
import psutil

def capture_true_data():
    current_time = time.strftime("%H:%M")
    net_io = psutil.net_io_counters()
    bandwidth_usage = net_io.bytes_sent + net_io.bytes_recv
    connections = psutil.net_connections()
    num_connections = len(connections)

    return f"Time: {current_time}, Bandwidth Usage: {bandwidth_usage}, Num Connections: {num_connections}"

# Capture true data
true_data = capture_true_data()

# Save data to a text file
with open('captured_data.txt', 'w') as file:
    file.write(true_data)