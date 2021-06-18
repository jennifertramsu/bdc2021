import pandas as pd
import re
import nltk

#from wordcloud import WordCloud, STOPWORDS
from PIL import Image
from textblob import TextBlob
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def clean_tweet(df, colname):
    
    # remove RT
    tweets = df[colname].map(lambda x: re.sub('RT @\w+: ', " ", x))
    # remove punctuation
    tweets = tweets.apply(func=lambda x : ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", x).split()))
    # lowercase
    tweets = tweets.apply(str.lower)
    # whatever the fuck x000d is
    tweets = tweets.apply(lambda x : re.sub("x000d ", " ", x))
    df["cleaned_tweet"] = tweets
    
    return df

def sentimentanalysis(df, col):

    df = clean_tweet(df, col)
    
    analysis = []
    subjectivity = []
    
    for tweet in df['cleaned_tweet']:
        senti = TextBlob(tweet)
        analysis.append(senti)

    df["polarity"] = [analysis[i].sentiment.polarity for i in range(len(analysis))]
    df['subjectivity'] = [analysis[i].sentiment.subjectivity for i in range(len(analysis))]
    
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
'''
def create_wordcloud(text):
    mask = np.array(Image.open("cloud.png"))
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white", mask = mask, max_words=3000, stopwords=stopwords, repeat=True)
    wc.generate(str(text))
    wc.to_file("Wordclouds/wc.png")
    path="wc.png"
    display(Image.open(path))
'''