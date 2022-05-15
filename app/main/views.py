from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .forms import *
from ..models import Blog,Comment
from .. import db
from ..requests import get_quote

from flask_login import login_required,current_user

from PIL import Image

@main.route('/')
def index():
    blog=Blog.query.all()
    quote = get_quote()

    return render_template('index.html', blog=blog, quote=quote)

@main.route('/addblog',methods=['GET','POST'])
@login_required
def add_blog():
    form = BlogForm()
    if form.validate_on_submit():
        new_blog = Blog(title=form.title.data, content=form.content.data, author=form.author.data) 
        db.session.add(new_blog)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('blog.html', form=form)

@main.route('/addcomment',methods=['GET','POST'])
@login_required
def add_comment():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(title=form.title.data, content=form.content.data, username=form.username.data) 
        db.session.add(new_comment)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template('addcomment.html', form=form)

@main.route('/viewcomments')
def viewcomments():
    comment = Comment.query.all()
    
    return render_template('viewcomments.html', comment = comment)

@main.route('/delete/comment/<comment_id>')
@login_required
def deleteComment(comment_id):
    comment = Comment.query.filter(Comment.id == comment_id).first()
    if not comment:
        flash('Comment not found', category='error')
    elif current_user.id != comment.user.id and  current_user.id != post.author.id:
        flash('YOu are not authorized to delete this comment', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()
    return redirect(url_for('main.index'))

@main.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated.','success')
        return redirect(url_for('main.account'))
    elif request.method =='GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account.html', title='Account', form = form)



