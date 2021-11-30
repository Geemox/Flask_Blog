# run this command to set the environment variable to the python file
# set FLASK_APP=flaskblog.py
# To run the flask application execute the following command
# flask run
# to run the server in debug mode set the following variable
# set FLASK_DEBUG=1

from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'c2a2cfc5e5f1191e953d0e6668db4086'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer, index=True)
    address = db.Column(db.String(256))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120), index=True)

db.create_all()

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

@app.route("/table")
def table():
    users = User.query
    return render_template('table.html', title='Table', users=users)

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
	app.run(debug=True)