# -*- coding: UTF-8 -*-
"""
app1f.py: Using functions redirect() and url_for()
"""
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('start', username='Peter'))
    # Also pass an optional URL variable

@app.route('/go/<username>')
def start(username):
    return 'Hello, %s' % username

if __name__ == '__main__':
    app.run(debug=True)