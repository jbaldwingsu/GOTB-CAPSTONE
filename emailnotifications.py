# refer to the README.md for directions on how to run this script

import smtplib
from email.mime.text import MIMEText

class EmailNotifications:
    def __init__(self, sender, recipients, password):
        self.sender = sender
        self.recipients = recipients
        self.password = password

    def send_summary(self, summary):
        subject = "GOTB SIEM Summary Report"
        body = summary
        self.send_email(subject, body)

    def send_alert(self, body):
        subject = "GOTB SIEM Alert"
        body = "An alert has been triggered by the SIEM system.\n"
        self.send_email(subject, body)

    def send_email(self, subject, body):
        msg = MIMEText(body, 'html')  # Specify that the body is HTML
        msg['Subject'] = subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(self.sender, self.password)
            smtp_server.send_message(msg)
        print(f"{subject} email sent to {msg['To']}")

# Usage:
# email_notifications = EmailNotifications(sender, recipients, password)
# email_notifications.send_summary()
# email_notifications.send_alert("Alert body")