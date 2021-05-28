import os
import pandas as pd
import numpy as np

os.chdir("/Users/sarinaxi/Desktop/UBDC2021/Usable Data/CTF Dataset Sample/")

def format_data(filename, name):
    col_list = ["id"]
    df = pd.read_csv(filename, usecols=col_list)
    dict = {}
    tweets = df["id"]
    np.savetxt(name, tweets, fmt=['%d'])

format_data("fake.csv", "fake.txt")
format_data("genuine.csv", "genuine.txt")
format_data("unlabelled.csv", "unlabelled.txt")
