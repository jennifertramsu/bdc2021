import twint
import sys

def scrape_tweets(names : list):
    
    c = twint.Config()

    for name in names:
        c.Username = name
        c.Store_csv = True
        c.Output = name + ".csv"
        c.Since = "2020-01-01"
        twint.run.Search(c)

names = []

# to call from command line
# --> >> python tweetScrapper <<name1>> <<name2>> ...
# otherwise, if editing script directly, add names to the list names

if len(sys.argv) > 1:
    for name in sys.argv:
        if name == "tweetScrapper.py":
            continue
        names.append(name)
   
scrape_tweets(names)

