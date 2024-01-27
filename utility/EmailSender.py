import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailSender:
    def __init__(self):
        self.smtp_server = "smtp.hostinger.com"
        self.smtp_port = 587
        self.smtp_username = "support@empchief.com"
        self.smtp_password = "&833NjKXpb7xjPLo"

    def send_email(self, subject, body):
        email_message = MIMEMultipart()
        email_message['From'] = self.smtp_username
        email_message['To'] = self.smtp_username
        email_message['Subject'] = subject
        email_message.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as smtp_server:
            smtp_server.starttls()
            smtp_server.login(self.smtp_username, self.smtp_password)
            smtp_server.sendmail(
                self.smtp_username, self.smtp_username, email_message.as_string())
