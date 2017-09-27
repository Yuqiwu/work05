import csv
import random

with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    d = {}
    c = 0
    for row in reader:
        d[ c ] =  [ row['Job Class'], row['Percentage'], row['Link'] ]
        c = c + 1

print d