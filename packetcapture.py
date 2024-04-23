import scapy.all as scapy
import datetime
import os
import dotenv
from emailnotifications import EmailNotifications

# Load .env file for email credentials
dotenv.load_dotenv()

# Create an instance of EmailNotifications
sender = os.getenv('SENDER')
recipients = [os.getenv('RECIPIENT')]
password = os.getenv('API_KEY')
email_notifications = EmailNotifications(sender, recipients, password)

# Function to check if a packet contains a critical security risk
def is_critical_security_risk(packet):
    # Check if the packet contains a suspicious string
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["password", "login", "user", "username", "pass", "key"]
        for keyword in keywords:
            if keyword.encode() in load:
                return True
    return False

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
    with open("network_log.txt", "a") as log_file:
        log_file.write(log_message)
    
    # Check for critical security risk
    if is_critical_security_risk(packet):
        rmessage = """
        <html>
        <head></head>
        <body>
            <p>Urgent,</p>
            <p>This is an automated message from the Guardians of the Binary SIEM: </p>
            <ul>
                <li>Our System detected a suspicous a packet. Please act now.</li>
            </ul>
            <p>Best regards,</p>
            <p>GOTB</p>
        </body>
        </html>
        """
        email_notifications.send_alert(rmessage)

# Creating a summary to be used for an email notification
def generate_summary():
    with open("network_log.txt", "r") as log_file:
        logs = log_file.readlines()

    total_packets = len(logs)
    tcp_packets = sum('TCP' in log for log in logs)
    udp_packets = sum('UDP' in log for log in logs)
    icmp_packets = sum('ICMP' in log for log in logs)

    # summary = f"Total packets: {total_packets}\nTCP packets: {tcp_packets}\nUDP packets: {udp_packets}\nICMP packets: {icmp_packets}"

    summary = f"""
    <html>
    <head></head>
    <body>
        <p>Hello,</p>
        <p>This is an automated Summary Report from the Guardians of the Binary SIEM:</p>
        <ul>
            <li>"Total packets: {total_packets}</li>
            <li>TCP packets: {tcp_packets}</li>
            <li>UDP packets: {udp_packets}</li>
            <li>ICMP packets: {icmp_packets}</li>
        </ul>
        <p>Best regards,</p>
        <p>GOTB</p>
    </body>
    </html>
    """
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
        # Generate a summary and send an email notification
        print("Packet capture has stopped.")
        summary = generate_summary()
        email_notifications.send_summary(summary)

if __name__ == "__main__":
    main()