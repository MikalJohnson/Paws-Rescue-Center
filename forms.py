from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo

class SignupForm(FlaskForm):
    fullName = StringField("Full Name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired(), EqualTo('confirmPassword', message="Passwords should match")])
    confirmPassword = PasswordField("Confirm Password", validators=[InputRequired()])
    submit = SubmitField("Sign Up")