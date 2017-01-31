import QnA
qQues=QnA.make_QnA()


from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('disp.html',qQues=qQues)

if __name__ == '__main__':
    app.run(debug=True)