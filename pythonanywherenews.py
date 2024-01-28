import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests
import os
import json

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

class NewsEmailer:
    def __init__(self):
        self.email_sender = EmailSender()
        self.api_key = os.environ.get("API_KEY")

    def read_recipients(self, file_path="data/recipients.json"):
        with open(file_path, "r") as file:
            recipients = json.load(file)
        return recipients

    def get_top_headlines(self, country, language, subject):
        news_api_url = f"https://newsapi.org/v2/top-headlines?" \
                   f"country={country}&" \
                   f"apiKey={self.api_key}&" \
                   f"language={language}"

        response = requests.get(news_api_url)

        if response.status_code == 200:
            news_content_list = []

            news_data = response.json()
            for article in news_data['articles']:
                article_details = (
                    f"Title: {article['title']}\n"
                    f"Description: {article['description']}\n"
                    f"URL: {article['url']}\n"
                    f"Published at: {article['publishedAt']}" + 2 * "\n"
                )
                news_content_list.append(article_details)

            combined_content = "\n".join(news_content_list)

            recipients = self.read_recipients()
            for recipient in recipients:
                email_body = f"Hello {recipient['name']},\n\n{combined_content}"
                success = self.email_sender.send_email(subject, email_body, recipient['email'])

                if success:
                    print(f"Email sent successfully to {recipient['name']} ({recipient['email']})!")
                else:
                    print(f"Failed to send email to {recipient['name']} ({recipient['email']}). Check the error message above.")
        else:
            print(f"News API request failed with status code {response.status_code}")

if __name__ == "__main__":
    news_emailer = NewsEmailer()
    news_emailer.get_top_headlines(country="no", language="no", subject="Top News Headlines in Norway")
    news_emailer.get_top_headlines(country="us", language="en", subject="Top News Headlines in United States")
