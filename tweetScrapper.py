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
    
    file = open("rightnews_followers", "w")
    
    file.write("user,followers\n")
        
    for name in names:
        c.Username = name
        c.Format = "{username},{followers}"
        twint.run.Lookup(c)

names = []

# to call from command line
# --> >> python tweetScrapper.py <<name1>> <<name2>> ...
# otherwise, if editing script directly, add names to the list names

if len(sys.argv) > 1:
    for name in sys.argv[1:]:
        names.append(name)
   
scrape_tweets(names)
