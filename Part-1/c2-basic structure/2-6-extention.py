# flask==1.1.4
# markupsafe==2.0.1
# flask-script

from flask import Flask

from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello, world!'


if __name__=='__main__':
    manager.run()