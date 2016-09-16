# -*- coding: UTF-8 -*-
"""
app1.py: First Python-Flask webapp
"""
from flask import Flask  # Import class Flask from module flask
app = Flask(__name__)    # Construct an instance of Flask class

@app.route('/')
def index():
   """Return an HTML-formatted string and an optional response status code"""
   return """<!DOCTYPE html>
      <html>
      <head><title>Hello</title></head>
      <body><h1>Hello, world!</h1></body>
      </html>""", 200


if __name__ == '__main__':  # Script executed directly?
   app.run()  # Launch built-in web server and run this Flask webapp
