from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/<user>')
def user(user):
    comments = ['felix', 'daniel', 'edon']
    return render_template('3-1-3-user.html', user=user, comments=comments)

@app.route('/')
def child():
    return render_template('3-1-3-child.html')

if __name__ == "__main__":
    app.run(debug=True)
