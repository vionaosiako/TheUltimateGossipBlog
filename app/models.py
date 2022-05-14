# from sqlalchemy import False
from app import db, login_manager

from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    email = db.Column(db.String(100),nullable = False,unique = True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(255))
        
    userblog = db.relationship('Blog',backref='user', lazy='dynamic')


    def __repr__(self):
        return f'User {self.username}'
    
class Blog(db.Model):
    __tablename__ = 'blogs'
    id = db.Column(db.Integer,primary_key = True)
    title= db.Column(db.String(255))
    content = db.Column(db.String(1000))
    author = db.Column(db.String(255))
        
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
    title= db.Column(db.String(255))
    content = db.Column(db.String(1000))
    username = db.Column(db.String(255))
        
    # user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
        
    def __repr__(self):
        return f'Comment {self.title}'
    