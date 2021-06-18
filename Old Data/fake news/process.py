import csv
import glob


with open('Datasets/fake news/CMUIDs.csv', 'w', newline = '') as csvWrite:
    writer = csv.writer(csvWrite, delimiter = ' ', quotechar='|')

    with open('Datasets/fake news/CMU_MisCov19_dataset.csv') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0].isnumeric():
                writer.writerow(line[0])
