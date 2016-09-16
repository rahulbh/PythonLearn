# -*- coding: UTF-8 -*-
"""
app1.py: First Python-Flask webapp
"""
from flask import Flask, render_template  # Need render_template to render HTML pages
app = Flask(__name__)    # Construct an instance of Flask class
app.debug = True  # Enable reloader and debugger

@app.route('/')
def index():
   """Return an HTML-formatted string and an optional response status code"""
   return render_template('index.html')  # To be placed under sub-directory templates


if __name__ == '__main__':  # Script executed directly?
   app.run()  # Launch built-in web server and run this Flask webapp
