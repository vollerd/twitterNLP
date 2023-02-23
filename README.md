# twitterNLP

A short example of NLP using the vader lexicon.

In this script, I utilize the VADER lexicon, a pre-trained sentiment analysis model, to classify tweets as positive, negative, or neutral. By creating an instance of the SentimentIntensityAnalyzer class, it's easy to obtain polarity scores for any given text, in this case fake tweets.

The classify_sentiment function takes a tweet as input, uses the SentimentIntensityAnalyzer to calculate polarity scores, and then returns a sentiment label based on a pre-defined threshold.

The sentiment label is determined based on a threshold of 0.05 for the compound score, which represents the overall sentiment of the tweet on a scale from -1 to 1. Finally, we can test the classifier with some sample tweets to ensure it's working correctly.

If the script were expanded, for example by scraping real tweets, it could be a simple tool for anyone interested in social media analysis or natural language processing.

