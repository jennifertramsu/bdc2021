import pandas as pd

ids = pd.read_csv("Dataset-I", sep="\t")

fake = ids[ids["tweet_class"].str.lower().str.contains("false")]

true = ids[ids["tweet_class"].str.lower().str.contains("true")]

with open("misinformation_fake_ids.txt", "w") as file:
    for l in fake["tweet_id"]:
        file.write(str(l) + "\n")

with open("misinformation_real_ids.txt", "w") as file:
    for l in true["tweet_id"]:
        file.write(str(l) + "\n")