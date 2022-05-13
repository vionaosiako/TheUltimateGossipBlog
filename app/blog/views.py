from . . import db
from . forms import BlogForm
from . import blog
from flask import render-template, redirect
from .. models import Blog

@blog.route('/addblog', method ['GET','POST'])
def add_blog():
    form = BlogForm
    if form.validate_on_submit():
        title= form.title.data
        content = form.content.data
        author = form.author.data
        new blog = Blog(title=title, content=content, author=author)
    
    return render_template('blog/blog.html', form=form)

    