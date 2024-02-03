import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

"""EmailSender class for sending emails via SMTP.

Provides a simple interface for constructing and sending email messages via SMTP.
Handles connecting to an SMTP server, constructing MIME messages, and sending.
"""


class EmailSender:
    def __init__(self):
        self.smtp_server = "smtp.hostinger.com"
        self.smtp_port = 587
        self.smtp_username = "support@empchief.com"
        self.smtp_password = "&833NjKXpb7xjPLo"

    def send_email(self, subject, body, to_email):
        print(f"Sending email to {to_email}...")
        email_message = MIMEMultipart()
        email_message['From'] = self.smtp_username
        email_message['To'] = to_email
        email_message['Subject'] = subject

        if isinstance(body, str):
            body = body.encode('utf-8')

        email_message.attach(MIMEText(body.decode('utf-8'), 'plain'))

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp_server:
                smtp_server.starttls()
                smtp_server.login(self.smtp_username, self.smtp_password)
                smtp_server.sendmail(
                    self.smtp_username, to_email, email_message.as_string())
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
