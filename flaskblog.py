# run this command to set the environment variable to the python file
# set FLASK_APP=flaskblog.py
# To run the flask application execute the following command
# flask run
# to run the server in debug mode set the following variable
# set FLASK_DEBUG=1

from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author': 'Firas Jrad',
		'title': 'Blog Post 1',
		'content': 'my first content',
		'date_posted': 'November 29, 2021'
	},
	{
		'author': 'Yohan Schwarz',
		'title': 'Blog Post 2',
		'content': 'my first content',
		'date_posted': 'November 30, 2021'
	}
]

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__ == '__main__':
	app.run(debug=True)