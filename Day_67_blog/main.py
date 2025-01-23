from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
from datetime import date
from flask_ckeditor import CKEditor
from datetime import datetime
import os

'''
Make sure the required packages are installed.
install the packages from the requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
app.config['CKEDITOR_PKG_TYPE'] = 'basic'
ckeditor = CKEditor(app)
Bootstrap5(app)

# CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db' #put your DB name
db = SQLAlchemy()
# db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=True)


with app.app_context():
    db.create_all()

# BlogPost Form
class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    img_url = StringField('Image URL')
    body = CKEditorField('Content', validators=[DataRequired()])
    submit = SubmitField('Publish Post')

def create_app():
    ckeditor.init_app(app)
    return app

@app.route('/', methods=["GET"])
def get_all_posts():
    # TODO: Query the database for all the posts. Convert the data to a python list.
    all_posts = db.session.query(BlogPost).all()
    for post in all_posts:
        post.body = ' '.join(post.body.split()[:50])
    return render_template("index.html", all_posts=all_posts)

# TODO: Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    # TODO: Retrieve a BlogPost from the database based on the post_id
    post = db.session.get(BlogPost, post_id)
    return render_template("post.html", post=post)


# TODO: add_new_post() to create a new blog post
@app.route('/new', methods=["GET"])
def new_post():
    form = BlogPostForm()
    return render_template("new-post.html", form=form)

@app.route('/create', methods=["POST"])
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                date=datetime.now().strftime("%B %d, %Y"),
                body=form.body.data,
                author=form.author.data,
                img_url=form.img_url.data
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))
    return render_template('new-post.html', form=form)

# TODO: edit_post() to change an existing blog post
@app.route('/edit/<int:post_id>', methods=["GET", "POST"])
def edit_post(post_id):
    form = BlogPostForm()
    # post_id = request.args.get("id")
    post = db.session.get(BlogPost, post_id)
    form = BlogPostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))
    return render_template("edit-post.html", post=post, form=form, is_edit=True)

# TODO: delete_post() to remove a blog post from the database
@app.route('/delete/<int:post_id>')
def delete_post(post_id):
    post=db.session.get(BlogPost, post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('get_all_posts'))

# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
