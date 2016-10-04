# -*- coding: UTF-8 -*-
"""
app1e.py: Using URL Variables
"""
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, world!'

@app.route('/hello/<username>')  # URL with a variable
def hello_user(username):        # The function shall take the URL variable as parameter
    return 'Hello, %s' % username

@app.route('/hello/<int:userid>')  # Variable with type filter. Accept only int
def hello_userid(userid):          # The function shall take the URL variable as parameter
    return 'Hello, your ID is: %d' % userid

if __name__ == '__main__':
    app.run(debug=True)  # Enable reloader and debugger