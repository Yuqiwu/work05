from flask import Flask, render_template
import csv
import random
		
my_app = Flask(__name__)

@my_app.route('/')
def root():
	return "Hi this is Yu Qi and Michela's page"

with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    d = {}
    c = 0
    for row in reader:
        d[ c ] =  [ row['Job Class'], row['Percentage'], row['Link'] ]
        c = c + 1

def randomPick(data):
    num = random.randint(0,21)
    for job in data:
        if num == job:
            return d[job]
	
@my_app.route('/occupations')
def occupations():
	obj = randomPick(d)
	occ = obj[0]
	pen = obj[1]
	lin = obj[2]
	return render_template('basic.html', occupation = occ, percent = pen, link = lin)

if __name__ == '__main__':
	my_app.debug = True
	my_app.run()
