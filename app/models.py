# from sqlalchemy import False
from app import db, login_manager

from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash

from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(100),nullable = False,unique = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
    bio = db.Column(db.String(500))
    image_file = db.Column(db.String(100), default='default.jpg')
        
    userblog = db.relationship('Blog',backref='user', lazy='dynamic')
    usercomment = db.relationship('Comment',backref='user', lazy='dynamic')


    def __repr__(self):
        return f'User {self.username}'
    
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title= db.Column(db.String(255))
    content = db.Column(db.String(1000))
    author = db.Column(db.String(255))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    usercomment = db.relationship('Comment',backref='blog', lazy='dynamic')        
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        
    def __repr__(self):
        return f'Blog {self.author}'
    
    #To get blogs
    @classmethod
    def get_blogs(cls,id):
        a_blog = Blog.query.filter_by(id=id).all
        return a_blog
        
    #To save the blog
    def save_blogs (self):
        db.session.add(self)
        db.session.commit()
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(1000))
            
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    
    #To save the comment
    def save_c (self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f'Comment {self.title}'
    
class Quote:
    """
    Class that returns quotes requested from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote
    