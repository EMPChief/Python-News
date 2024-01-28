from utility import NewsEmailer
import time
if __name__ == "__main__":
    news_emailer = NewsEmailer()
    news_emailer.get_top_headlines(country="no", language="no", subject="Top News Headlines in Norway")
    print("Sleeping for 60 seconds before sending the next email...")
    time.sleep(60)
    news_emailer.get_top_headlines(country="us", language="en", subject="Top News Headlines in United States")
    print("Script finished.")
