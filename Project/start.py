from flask import Flask, render_template, request
from insert_login import insert_login

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Read the HTTP POST request parameter from request.form
    user = request.form['mailid']
    password = request.form['pass']
    option = request.form['option']
    # Validate and send response
    if (user and password and option):
        flag=insert_login(user,password,option)
        if flag==0:
            return render_template('index.html')
        else:
            return render_template('loggedin.html')
    else:
        return 'Please go back and enter the details...'
        
if __name__ == '__main__':
    app.run(debug=True)
