# -*- coding: UTF-8 -*-
"""(controller1.py) Flask-WTF Example 1: app controller"""
from flask import Flask, render_template
from forms1 import LoginForm

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-SECRET'  # Flask-WTF: Needed for CSRF

@app.route('/')
def index():
   # Construct an instance of LoginForm
   form = LoginForm()

   # Render an HTML page, with the login form instance created
   return render_template('login1.html', form=form)

if __name__ == '__main__':
   app.run(debug=True)