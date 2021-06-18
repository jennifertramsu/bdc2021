import pandas as pd
import glob
import datetime

# new filter

def filter_data(type, strings):
    ''' Reads in excel files from directory type and returns the final concatenated dataframe. '''
    
    df_path = glob.glob('./Datasets/' + str(type) + '/*.csv')
    df_ls = []
    
    for path in df_path:
        try:
            df = pd.read_csv(path)
            df = df[['username', 'tweet','date', 'replies_count','retweets_count','likes_count','hashtags','retweet']]
            covid = df.loc[df['tweet'].str.contains(strings, case=False)]
            df_ls.append(covid)
        except:
            df = pd.read_csv(path)
            df = df[["user_name", "user_screen_name", "text", "created_at", "retweet_count", "favorite_count", "hashtags", "user_followers_count", "user_verified"]]
            covid = df.loc[df['text'].str.contains(strings, case=False)]
            df_ls.append(covid)
        
    finaldf = pd.concat(df_ls, ignore_index = True)
    
    return finaldf

# filter for tweets in first half of 2020

def filter_dates(df):
    ''' Filter for tweets between March 3, 2020 and May 25, 2020. '''
    
    dates = []
    try:
        for date in df["date"]:
            temp = datetime.datetime.strptime(date, "%Y-%m-%d")
            dates.append(temp.date())
        
        df["date"] = dates
        
    except:
        dates = df["created_at"]
        dates = [date[4:10] + " " + date[-4:] for date in dates]

        for i in range(len(dates)):
            temp = datetime.datetime.strptime(dates[i], "%b %d %Y")
            dates[i] = temp.date()

        # reassigned back to df

        df["date"] = dates
        df = df.drop("created_at", axis=1)
    
    df = df[df["date"] <= datetime.date(2020,5,25)]
    df = df[df["date"] >= datetime.date(2020,3,1)]
    
    return df
