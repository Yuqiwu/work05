import csv
import random

with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    d = {}
    c = 0
    for row in reader:
        d[ (c, c + float (row['Percentage']))  ] =  row['Job Class']
        c = c + float(row['Percentage'])

#for job in d:
#    print (job , d[job])    

def randomPick(data):
    num = random.random() * 99.8
    for job in data:
        if num > job[0] and num <= job[1]:
            return d[job]
            
print randomPick(d)
    
