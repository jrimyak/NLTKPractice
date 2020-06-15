from nltk.corpus import twitter_samples
print(twitter_samples.fileids())

# Getting the data from the positive_tweets
# List should have 5000 tweets
pos_tweets = twitter_samples.strings('positive_tweets.json')
print(len(pos_tweets))

# Getting the data from the positive_tweets
# List should have 5000 tweets
neg_tweets = twitter_samples.strings('negative_tweets.json')
print(len(neg_tweets))

# Getting the data for all tweets
# List should have 20000 tweets
all_tweets = twitter_samples.strings('tweets.20150430-223406.json')
print(len(all_tweets))

# Printing the first 5 positive tweets
for tweet in pos_tweets[:5]:
    print(tweet)
