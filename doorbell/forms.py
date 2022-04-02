from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired
from doorbell.models import User

class LoginForm(FlaskForm):
    username = StringField("Username", 
        validators = [
            DataRequired(),
            ])
    password = PasswordField("Password", 
        validators = [
            DataRequired(), 
            ])
    submit = SubmitField("Login")

    def validate_username(self, username):
        username = User.query.filter_by(username = username.data).first()
        if not username:
            raise ValidationError("Username is not registered.")
