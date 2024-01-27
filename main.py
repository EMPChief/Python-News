from utility import NewsEmailer

if __name__ == "__main__":
    news_emailer = NewsEmailer()
    news_emailer.get_top_headlines(country="no", language="no", subject="Top News Headlines in Norway")
    news_emailer.get_top_headlines(country="us", language="en", subject="Top News Headlines in United States")
