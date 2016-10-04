# -*- coding: UTF-8 -*-
"""(app.py) Testing Flask's session"""
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Your Secret Key'

@app.route('/')
def index():
   if 'username' in session:
      return 'You are already logged in as %s' % escape(session['username'])
            # Escape special HTML characters (such as <, >) in echoing to prevent XSS
   return (redirect(url_for('login')))

@app.route('/login', methods=['GET', 'POST'])
def login():
   # for the initial GET request
   if request.method == 'POST':
      username = request.form['username']
      session['username'] = username   # Save in session
      return 'Logined in as %s' % escape(username)

   # for subsequent POST request
   return '''
      <form method='POST'>
         <input type='text' name='username'>
         <input type='submit' value='Login'>
      </form>'''

@app.route('/logout')
def logout():
    # Remove the username from the session if it exists
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug=True)