import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# download the necessary NLTK data
nltk.download('vader_lexicon')

# create an instance of the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# define a function to classify a tweet's sentiment
def classify_sentiment(tweet):
    # use the sentiment analyzer to get the polarity scores for the tweet
    scores = sia.polarity_scores(tweet)
    # determine the sentiment label based on the polarity scores
    if scores['compound'] > 0.05:
        return 'Positive'
    elif scores['compound'] < -0.05:
        return 'Negative'
    else:
        return 'Neutral'

tweets = ["I love this movie! It's so funny.", "The red wine is more expensive than the white.", "That pidgeon ate my sandwich.", "You're crazy if you believe him."]

# test the sentiment classifier
for tweet in tweets: 
    sentiment = classify_sentiment(tweet)
    print(f"\n'{tweet}' - {sentiment}") 

 