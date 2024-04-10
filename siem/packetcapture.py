import scapy.all as scapy
import datetime

def packet_callback(packet):
    # Log packet details (customize as needed)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    source_ip = packet[scapy.IP].src
    destination_ip = packet[scapy.IP].dst
    protocol_num = packet[scapy.IP].proto

    # Map protocol numbers to names
    protocols = {1: 'ICMP', 6: 'TCP', 17: 'UDP'}
    protocol = protocols.get(protocol_num, 'Unknown')

    log_message = f"{timestamp}, {source_ip}, {destination_ip}, {protocol}\n"

    # Append the log message to a file
    with open("siem/network_log.txt", "a") as log_file:
        log_file.write(log_message)

def main():
    # Start sniffing the network
    scapy.sniff(filter="ip", prn=packet_callback)

if __name__ == "__main__":
    main()