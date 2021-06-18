import csv
import glob


with open('Datasets/Covid19-Lies/covid_lies_id.csv', 'w', newline = '') as csvWrite:
    writer = csv.writer(csvWrite, delimiter = ' ', quotechar='|')

    with open('Datasets/Covid19-Lies/covid_lies.csv') as csvfile:
        reader = csv.reader(csvfile)
        for line in reader:
            if line[0].isnumeric():
                writer.writerow(line[2])
