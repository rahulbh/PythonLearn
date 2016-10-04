# -*- coding: UTF-8 -*-
"""(controller2.py) Flask-WTF Example 2: Processing the Login Form"""
from flask import Flask, render_template, request, flash, redirect, url_for
from forms2 import LoginForm

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-SECRET'  # Flask-WTF: Needed for CSRF

@app.route('/', methods=['get', 'post'])  # Initial request via GET, subsequently POST
def index():
   form = LoginForm()  # Construct an instance of LoginForm

   if form.validate_on_submit():  # POST request with valid input?
      # Verify username and passwd
      if (form.username.data == 'Peter' and form.passwd.data == 'xxxx'):
         return redirect(url_for('start_app'))
      else:
         # Using Flask's flash to output an error message
         flash(u'Username or password incorrect')

   # For the initial GET request, and subsequent invalid POST request,
   # render an HTML page, with the login form instance created
   return render_template('login2.html', form=form)

@app.route('/start_app')
def start_app():
   return 'The app starts here!'

if __name__ == '__main__':
   app.run(debug=True)