from flask import Flask, session, render_template, url_for, redirect
from flask_bootstrap import Bootstrap
from form4 import NameForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'secret!'

# 将用户名存储在session中，可以跨request 共享数据
# 使用redirect 和 url_for 重定向请求提交数据后的页面
@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

if __name__ == '__main__':
    app.run(debug=True)