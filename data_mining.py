import tweepy
from config import consumer_key, consumer_secret, access_key, access_secret
import pandas as pd
import csv


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('../kaggle_data/tweet_scrapping_for_bots.csv', 'a')
csvWriter = csv.writer(csvFile)

search_words = "bot OR b0t OR fake account OR follow me OR tweet me OR fuck OR kill OR troll OR cunt OR nerd OR anon OR slag"  # enter your words
new_search = search_words + " -filter:retweets"

for tweet in tweepy.Cursor(api.search_tweets, q=new_search, count=1000,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.user.id,
                                       tweet.user.id_str,
                                       tweet.user.screen_name.encode('utf-8'),
                                       tweet.user.location.encode('utf-8'),
                                       tweet.user.description.encode('utf-8'),
                                       tweet.text.encode('utf-8'),
                                       tweet.user.followers_count,
                                       tweet.user.friends_count,
                                       tweet.user.listed_count,
                                       tweet.created_at,
                                       tweet.user.favourites_count,
                                       tweet.user.verified,
                                       tweet.user.statuses_count,
                                       tweet.lang.encode('utf-8'),
                                       tweet.user.default_profile,
                                       tweet.user.default_profile_image,
                                       tweet.user.has_extended_profile,
                                       tweet.user.name.encode('utf-8')
                                       ])

print("Completed!")
