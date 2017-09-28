from flask import Flask, render_template
from utils import work03
import csv
import random
		
my_app = Flask(__name__)

@my_app.route('/')
def root():
	return "Hi this is Yu Qi and Michela's page"
	
@my_app.route('/occupations')
def occupations():
	obj = work03.randomPick(work03.d)
	return render_template('basic.html', info = work03.d, choice = obj)

if __name__ == '__main__':
	my_app.debug = True
	my_app.run()
