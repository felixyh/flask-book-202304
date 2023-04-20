from flask import Flask, request, render_template

from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == "__main__":
    manager.run()