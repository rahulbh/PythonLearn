# -*- coding: UTF-8 -*-
"""Defining Context Variables for all Views"""
from flask import Flask, render_template, session
app = Flask(__name__)

@app.context_processor
def template_context():
   '''Return a dictionary of key-value pairs,
      which will be available to all views in the context'''
   if 'username' in session:
      username = session['username']
   else:
      username = 'Peter'

   return {'version':88, 'username':username}

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)