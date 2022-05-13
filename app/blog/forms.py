from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo,ValidationError
from app.models import Blog

class BlogForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])