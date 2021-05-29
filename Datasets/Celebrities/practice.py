import twint
import sys
import glob
import pandas as pd

def scrape_tweets(names : list):
    
    c = twint.Config()

    for name in names:
        c.Username = name
        c.Store_csv = True
        c.Output = name + ".csv"
        c.Since = "2020-01-01"
        twint.run.Search(c)

def scrape_followers(names : list):
    
    c = twint.Config()
    
    file = open("news_followers", "w")
    
    file.write("user,followers\n")
        
    for name in names:
        c.Username = name
        c.Format = "{username},{followers}"
        twint.run.Lookup(c)

names = []

"""path = "./Datasets/News_Outlets/*"

files = glob.glob(path)

dfs = [pd.read_csv(file) for file in files if "processing" not in file]

usernames = []

for df in dfs:
    try:
        user = df["username"].iloc[0]
    except:
        user = df["user_name"].iloc[0]
    
    usernames.append(user)
    
names = usernames"""

# to call from command line
# --> >> python tweetScrapper.py <<name1>> <<name2>> ...
# otherwise, if editing script directly, add names to the list names

if len(sys.argv) > 1:
    for name in sys.argv:
        if name == "practice.py":
            continue
        names.append(name)
   
scrape_tweets(names)
