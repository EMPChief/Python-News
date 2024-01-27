import requests
import os
from .EmailSender import EmailSender

class NewsEmailer:
    def __init__(self):
        self.email_sender = EmailSender()
        self.api_key = os.environ.get("API_KEY")

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

            success = self.email_sender.send_email(subject, combined_content)

            if success:
                print(f"Email sent successfully for {country}!")
            else:
                print(f"Failed to send email for {country}. Check the error message above.")
        else:
            print(f"News API request failed with status code {response.status_code}")