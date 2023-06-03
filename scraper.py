"""Scraping 100 tweets"""
import pandas as pd
import snscrape.modules.twitter as sntwitter

tweets = []

# Buscar los 100 tweets más recientes con el término "boric"
scraper = sntwitter.TwitterSearchScraper("boric")

for i, tweet in enumerate(scraper.get_items()):
    data = [
        i + 1,
        tweet.content.replace('\n', ' '),
    ]
    tweets.append(data)
    if i >= 99:
        break

tweet_df = pd.DataFrame(tweets, columns=['enumeration', 'content'])
tweet_df.to_csv('tweets.csv', index=False, encoding='utf-8')
