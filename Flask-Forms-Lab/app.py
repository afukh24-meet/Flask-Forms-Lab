from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "afu07"
password = "040107"
facebook_friends=["Loai","adi","saba", "celine", "majd", "haddad"]


@app.route('/',methods = ['GET' , 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		user = request.form['username']
		pas = request.form['password']
		if user == username and pas == password :
			return(redirect(url_for('home')))
	else:
		return render_template('login.html')

@app.route('/home')
def home():
		return render_template('home.html',friends = facebook_friends )


@app.route('/friend_exists/<string:name>',methods = ['GET' , 'POST'])
def hello_name_route(name):
  return render_template('friend_exists.html', n = name,friends = facebook_friends)


  



if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)