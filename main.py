import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import os


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


def main():
    email_sender = EmailSender()
    API_KEY = os.environ.get("API_KEY")
    print("Sending email...")

    news_api_url = f"https://newsapi.org/v2/top-headlines?country=no&apiKey={API_KEY}"
    response = requests.get(news_api_url)

    if response.status_code == 200:
        news_content = response.content.decode('utf-8')
        try:
            email_sender.send_email("News API Content", news_content)
            print("Email with News API content sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")
    else:
        print(
            f"News API request failed with status code {response.status_code}")


if __name__ == "__main__":
    main()
