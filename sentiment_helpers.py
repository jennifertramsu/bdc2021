import pandas as pd
import re
from textblob import TextBlob

def clean_tweet(df, colname):
    
    tweets = df[colname].apply(func=lambda x : ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x).split()))
    df["cleaned_tweet"] = tweets
    
    return df

def sentimentanalysis(df, col):

    df = clean_tweet(df, col)
    
    analysis = []
    
    for tweet in df['cleaned_tweet']:
        senti = TextBlob(tweet)
        analysis.append(senti)

    df["polarity"] = [analysis[i].sentiment.polarity for i in range(len(analysis))]

    def classify(analysis):
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    df["sentiment"] = [classify(a) for a in analysis]
    
    return df
