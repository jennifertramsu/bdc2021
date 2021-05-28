import pandas as pd

# grabbing tweet ids to hydrate

fake = pd.read_csv("fake.csv", index_col=0)
real = pd.read_csv("genuine.csv", index_col=0)

file1 = open("fake_ids.txt", "w")
file2 = open("real_ids.txt", "w")

for line in fake["id"]:
    file1.write(str(line) + "\n")
    
for line in real["id"]:
    file2.write(str(line) + "\n")