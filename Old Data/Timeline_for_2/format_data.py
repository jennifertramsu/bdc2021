import os
import pandas as pd
import numpy as np

## Get individual events
def format_data_individual(filenname, directionry):
    col_list = ["index", "tweet_id"]
    df = pd.read_csv(filename, usecols=col_list)
    dict = {}
    index = df["index"]
    tweets = df["tweet_id"]
    for i in range(len(index)):
        val = dict.get(index[i], 0)
        if val == 0:
            dict[index[i]] = [tweets[i]]
        else:
            list = dict[index[i]]
            list.append(tweets[i])
            dict[index[i]] = list
    for key, values in dict.items():
        np.savetxt(directory + str(key), values, fmt=['%d'])

##
file_master = "/Users/sarinaxi/Desktop/UBDC2021/CoAID-master/"
date = ["05-01-2020", "07-01-2020", "09-01-2020", "11-01-2020"]
type = ["ClaimFake", "ClaimReal", "NewsFake", "NewsReal"]
file = "COVID-19_tweets.csv"
for i in date:
    for j in type:
        filename = file_master + i + "/" + j + "/" + j + file
        directory = file_master + i + "/" + j + "/"
        if os.path.isfile(filename) is True:
            format_data_individual(filename, directory)

## Get all tweets together within a category
def format_data_total(filenname, directionry):
    col_list = ["index", "tweet_id"]
    df = pd.read_csv(filename, usecols=col_list)
    dict = {}
    index = df["index"]
    tweets = df["tweet_id"]
    for i in range(len(index)):
        val = dict.get(index[i], 0)
        if val == 0:
            dict[index[i]] = [tweets[i]]
        else:
            list = dict[index[i]]
            list.append(tweets[i])
            dict[index[i]] = list
    lengths = []
    all_id = []
    events = []
    for key, values in dict.items():
        lengths.append(len(values))
        all_id = all_id + values
        events.append(key)
    np.savetxt(directory + "all_id.txt", all_id, fmt=['%d'])
    np.savetxt(directory + "lengths.txt", lengths, fmt=['%d'])
    np.savetxt(directory + "events.txt", events, fmt=['%d'])

##
file_master = "/Users/sarinaxi/Desktop/UBDC2021/CoAID-master/"
date = ["05-01-2020", "07-01-2020", "09-01-2020", "11-01-2020"]
type = ["ClaimFake", "ClaimReal", "NewsFake", "NewsReal"]
file = "COVID-19_tweets.csv"

for i in date:
    for j in type:
        filename = file_master + i + "/" + j + "/" + j + file
        directory = file_master + i + "/" + j + "/"
        if os.path.isfile(filename) is True:
            format_data_total(filename, directory)




