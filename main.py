import requests
import os
from utility import EmailSender


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
