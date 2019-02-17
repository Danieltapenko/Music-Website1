from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
class EmailForm(FlaskForm):
    submit = SubmitField('Join')
    logout = SubmitField('Log out')

class SignupForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    checkbox = BooleanField('Would you want to use this email to receive newsletters?')
    submit = SubmitField('JOIN!')

class LoginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Login!')

class BlogForm(FlaskForm):
    post = TextAreaField('Say a post!', validators=[Length(min=4,max=160)])
    submit = SubmitField('Submit',validators=LoginRequired())