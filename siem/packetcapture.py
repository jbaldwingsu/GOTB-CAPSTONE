import scapy.all as scapy
import datetime
import subprocess
import os

def packet_callback(packet):
    # Log packet details (customize as needed)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    source_ip = packet[scapy.IP].src
    destination_ip = packet[scapy.IP].dst
    protocol_num = packet[scapy.IP].proto

    # Map protocol numbers to names
    protocols = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
    protocol = protocols.get(protocol_num, 'Unknown')

    log_message = f"{timestamp} -  {source_ip},  {destination_ip}, : {protocol}\n"

    # Append the log message to a file
    with open("network_log.txt", "a") as log_file:
        log_file.write(log_message)

# Creating a summary to be used for an email notification
def generate_summary():
    with open("network_log.txt", "r") as log_file:
        logs = log_file.readlines()

    total_packets = len(logs)
    tcp_packets = sum('TCP' in log for log in logs)
    udp_packets = sum('UDP' in log for log in logs)
    icmp_packets = sum('ICMP' in log for log in logs)

    summary = f"Total packets: {total_packets}\nTCP packets: {tcp_packets}\nUDP packets: {udp_packets}\nICMP packets: {icmp_packets}"
    return summary

def main():
    print("Packet capture has started ... (Ctrl+C to stop)")
    try:
        # Start sniffing the network
        scapy.sniff(filter="ip", prn=packet_callback)
    except Exception as e:
        # If an error occurs while sniffing, print the error
        print(f"Error: {e}")
    finally:
        # Run emailsummary.py after packet capture terminates
        script_dir = os.path.dirname(os.path.realpath(__file__))
        email_script_path = os.path.join(script_dir, 'emailsummary.py')
        subprocess.run(["python", email_script_path])

if __name__ == "__main__":
    main()