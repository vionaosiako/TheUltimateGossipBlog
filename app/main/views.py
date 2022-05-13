from flask import render_template,request,redirect,url_for,abort,flash
from . import main
# from ..requests import 
from .forms import *
from ..models import Blog,Comment
from .. import db

# from flask_login import login_required,current_user

@main.route('/')
def index():
    blog=Blog.query.all()

    return render_template('index.html', blog=blog)

@main.route('/addblog',methods=['GET','POST'])
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(title=form.title.data, content=form.content.data, author=form.author.data) 
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('blog.html', form=form)

@main.route('/addcomment',methods=['GET','POST'])
def add_addcomment():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(title=form.title.data, content=form.content.data, username=form.username.data) 
        db.session.add(new_comment)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('addcomment.html', form=form)

    
