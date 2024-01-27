import requests
import os
from utility import EmailSender

def main():
    email_sender = EmailSender()
    api_key = os.environ.get("NEWS_API_KEY")

    print("Sending email...")

    news_api_url = f"https://newsapi.org/v2/top-headlines?country=no&apiKey={api_key}"
    response = requests.get(news_api_url)

    if response.status_code == 200:
        news_content_list = []

        news_data = response.json()
        for article in news_data['articles']:
            article_details = (
                f"Title: {article['title']}\n"
                f"Description: {article['description']}\n"
                f"URL: {article['url']}\n"
                f"Published at: {article['publishedAt']}\n"
            )
            news_content_list.append(article_details)

        combined_content = "\n".join(news_content_list)

        try:
            email_sender.send_email("Top News Headlines", combined_content)
            print("Email with News API content sent successfully!")
        except Exception as e:
            print(f"Error sending email: {e}")

    else:
        print(f"News API request failed with status code {response.status_code}")

if __name__ == "__main__":
    main()
