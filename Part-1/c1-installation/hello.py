from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_agent = request.headers.get('User-Agent')
    currentapp = current_app.name
    return '<p>Your browser is %s, current app is %s</p>' % (user_agent, currentapp)

if __name__=='__main__':
    app.run(debug=True)