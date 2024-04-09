# refer to the README.md for directions on how to run this script

import smtplib
from email.mime.text import MIMEText
from packetcapture import generate_summary

subject = "GOTB SIEM Summary Report"
body = "This is a summary of the network traffic captured by the SIEM system.\n" + generate_summary()
sender = "example@gmailexample.com"
recipients = ["example@georgiasouthernexample.edu"]
password = ""


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Summary email sent to " + msg['To'])


send_email(subject, body, sender, recipients, password)