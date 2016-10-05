# -*- coding: UTF-8 -*-
"""jinja_app1.py: Get start with Jinja2 templates"""
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Read the HTTP POST request parameter from request.form
    _username = request.form['username']
 
    # Validate and send response
    if _username:
        return render_template('response.html', username=_username)
    else:
        return 'Please go back and enter your name...'

if __name__ == '__main__':
    app.run(debug=True)