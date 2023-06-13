from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, email

class LoginForm(FlaskForm):
    email = StringField('email', validators = [InputRequired(), email()])
    password = PasswordField('password')
    submit = SubmitField('submit')