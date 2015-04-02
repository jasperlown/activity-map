from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Rex'} #fake user
	events = [
		{
			'author': {'nickname': 'Rex'},
			'eventTitle': 'Server Group Meeting',
			'startTime': '5:00pm',
			'locationName': 'Grainger Library'
		},
		{
			'author': {'nickname': 'Eddie'},
			'eventTitle': 'Server Group Party',
			'startTime': '8:00pm',
			'locationName': 'LAR Main Lounge'
		}
	]
	return render_template('index.html', title='Home', user=user, events=events)

@app.route('/login', methods=['GET','POST'])
def login():
	form = LoginForm()
	return render_template('login.html', title='Sign In', form=form)