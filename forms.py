from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class SignupForm(FlaskForm):
    fullname = StringField('Full Name:', validators=[InputRequired()])
    email = StringField('Email:', validators=[InputRequired(), Email()])
    password = PasswordField('Password:', validators=[InputRequired(), EqualTo('c_password', message='Password must match')])
    c_password = PasswordField('Confirm Password:', validators=[InputRequired()])
    submit = SubmitField('Submit')