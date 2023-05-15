from flask import Flask

# 跨站请求伪造保护 CSRF
app = Flask('__name__')
app.config['SECRET_KEY'] = 'hard to guess string'
