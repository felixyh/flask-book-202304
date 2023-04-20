from flask import Flask, request, make_response, redirect, abort

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return '<p>Bad Request', 400

@app.route('/makeresponse')
def makeresponse():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirectpage', methods=['GET', 'POST'])
def redirectpage():
    return redirect('http://www.example.com')

@app.route('/user/<id>')
def get_user(id):
    if int(id) <= 10:
        abort(404)
    return '<h1>Hello, %s</h1>' %id

if __name__=='__main__':
    app.run(debug=True)