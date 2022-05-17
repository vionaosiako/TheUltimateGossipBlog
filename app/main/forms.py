from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo,ValidationError
from app.models import Blog,Comment,User
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user


class BlogForm(FlaskForm):
    title= StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    submit = SubmitField('Add blog')
    
class CommentForm(FlaskForm):
    comment = TextAreaField('Write a Comment', validators=[DataRequired()])
    submit = SubmitField('Add Comment')
    
class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png'])])
    bio =TextAreaField('About yourself', validators=[DataRequired()])
    submit = SubmitField('Update')
    def validate_username(self,username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. PLease choose a different one.')
    def validate_email(self,email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. PLease choose a different one.')
    
