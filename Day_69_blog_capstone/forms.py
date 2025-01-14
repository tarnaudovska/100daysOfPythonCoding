from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, PasswordField, validators, ValidationError
from wtforms.validators import DataRequired, URL, InputRequired, EqualTo
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

# RegisterForm to register new users
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = EmailField("Email", validators=[InputRequired("Please enter your email address")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Sign me up')

# LoginForm to login existing users
class LoginForm(FlaskForm):
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address.")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Let me in')

# CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")

