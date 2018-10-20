from app import app
# from app.models import Employee
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
	test_data = 'Hello world!'
	# test_data = Employee.query.get(1) 
	return render_template('index.html', data=test_data)
