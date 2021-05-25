##  List of data from CSV file (34 parameters)
# coordinates                     created_at                      hashtags
# media                           urls                            favorite_count
# id                              in_reply_to_screen_name         in_reply_to_status_id
# in_reply_to_user_id             lang                            place
# possibly_sensitive              retweet_count                   retweet_id
# retweet_screen_name             source                          text
# tweet_url                       user_created_at                 user_screen_name
# user_default_profile_image      user_description                user_favourites_count
# user_followers_count            user_friends_count              user_listed_count
# user_location                   user_name                       user_screen_name.1
# user_statuses_count             user_time_zone                  user_urls
# user_verified

## Retrieve data and create timeline for general categories (fake/real news/claims)
import datetime
from matplotlib import pyplot as plt
import json
import os
import pandas as pd
import numpy as np
import time

os.chdir("/Users/sarinaxi/Desktop/UBDC2021/CoAID-master/05-01-2020/ClaimFake/")
filename = "all_id.csv"

def plot_timeline(filename, directory):
    col_list = ["created_at"]
    df = pd.read_csv(filename, usecols = col_list)
    dates = df[col_list[0]]
    formatted_dates = []
    for i in dates:
        formatted = i[4:20] + i[-4:]
        datetime_obj = datetime.datetime.strptime(formatted, '%b %d %H:%M:%S %Y')
        formatted_dates.append(datetime_obj)

    bin_num = max(1, min(len(formatted_dates), np.abs(int(len(formatted_dates)/10))))

    plt.hist(formatted_dates, bins = bin_num)
    plt.xticks(fontsize = 5)
    plt.savefig(directory + '/general_timeline.png')
    plt.close()
    print("Finished")

file_master = "/Users/sarinaxi/Desktop/UBDC2021/CoAID-master/"
date = ["05-01-2020", "07-01-2020", "09-01-2020", "11-01-2020"]
type = ["ClaimFake", "ClaimReal", "NewsFake", "NewsReal"]
file = "all_id.csv"
for i in date:
    for j in type:
        filename = file_master + i + "/" + j + "/" + file
        directory = file_master + i + "/" + j + "/" + "Figures"
        if os.path.isfile(filename) is True:
            plot_timeline(filename, directory)

##
plot_timeline("/Users/sarinaxi/Desktop/UBDC2021/CoAID-master/09-01-2020/NewsFake/all_id.csv", "/Users/sarinaxi/Desktop/UBDC2021/CoAID-master/09-01-2020/NewsFake/Figures")

