import twint

names = """joebiden
FoxNews
CNN
BBC
BorisJohnson
JustinTrudeau
jacindaardern
washingtonpost
CBCNews
VICE
charliekirk11
RealCandaceO
michaeljknowles
RubinReport
andrewklavan
JeremyDBoreing"""

names = names.split(sep="\n")

def scrape_tweets(names : list):
    
    c = twint.Config()

    for name in names:
        c.Username = name
        c.Store_csv = True
        c.Output = name + ".csv"
        c.Since = "2020-01-01"
        twint.run.Search(c)