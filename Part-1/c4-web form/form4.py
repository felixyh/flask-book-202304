# import FlaskForm, as Form is not supported in new flask_wtf
# 具体是Form 还是 FlaskForm根据自己的项目情况版本来决定 
# 这里注意下：from flask_wtf import FlaskForm,validators里是DataRequired，
# 如果是from flask_wtf import Form 就对应是 Required了

# from flask_wtf import Form


from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NameForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=20)])
    submit = SubmitField('Submit')