from flask_wtf import Form
from wtforms import StringField, PasswordField, validators, SubmitField
from wtforms.validators import DataRequired, Length, Email, InputRequired

class NameForm(Form):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Submit')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
