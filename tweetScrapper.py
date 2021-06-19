import twint
import sys
import getopt

# to call from command line
# --> >> python tweetScrapper.py -t <<name1>> <<name2>> ... for tweets 
# --> >> python tweetScrapper.py --tweets <<name1>> <<name2>> ... for tweets
# --> >> python tweetScrapper.py -f <<name1>> <<name2>> ... for followers
# --> >> python tweetScrapper.py -followers <<name1>> <<name2>> ... for followers

arguments = sys.argv[1:]
short_options = "tf"
long_options = ["tweet", "followers"]

# validating command-line flags and arguments
try:
    args, names = getopt.getopt(arguments, short_options, long_options) # args = flags, values = arguments
except getopt.error as e:
    print(str(e))
    sys.exit(2)

def scrape_tweets(names : list):
    
    print("Scraping tweets...\n")
    c = twint.Config()
    
    for name in names:
        c.Username = name
        c.Store_csv = True
        c.Output = name + ".csv"
        c.Since = "2020-01-01"
        twint.run.Search(c)

def scrape_followers(names : list):
    # pipe output to text file
    print("Scraping followers...\n")
    c = twint.Config()
    
    sys.stdout = open("followers.txt", "w")
    print("user,followers")
    for name in names:
        c.Username = name
        c.Format = "{username},{followers}"
        twint.run.Lookup(c)
    sys.stdout.close()
        
for a, v in args:
    if a in ("-t", "--tweet"):
        scrape_tweets(names)
    elif a in ("-f", "--followers"):
        scrape_followers(names)
