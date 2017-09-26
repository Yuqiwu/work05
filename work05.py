from flask import Flask, render_template
import csv

with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    d = {}
    for row in reader:
        d[ row['Job Class'] ]= row['Percentage']

my_app = Flask(__name__)

@my_app.route('/occupations')
def occupations():
	#{% block table %}
	
	#{% endblock %}
	return render_template('basic.html')

if __name__ == '__main__':
	my_app.debug = True
	my_app.run()
