from flask import Flask, render_template, session, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, EmailField, PasswordField, validators, ValidationError
from wtforms.validators import DataRequired, URL, InputRequired, EqualTo
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = '0511'

# CREATE DATABASE

class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
# db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB


class User(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()

class UserLogInForm(FlaskForm):
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address.")])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField('Let me in')
    
class UserRegister(FlaskForm):
    email = EmailField("Email",  validators=[InputRequired("Please enter your email address.")])
    password = StringField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField('Sign me up')

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    form = UserRegister()
    if form.validate_on_submit():
        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = form.password.data
        )

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    print(request.method)
    form=UserLogInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and password==user.password:
            session['user_id'] = user.id
            flash("Login successful", "success")
            return redirect(url_for('secrets'))
        else:
            flash("Invalid email or password", "error")

        
    return render_template("login.html", form=form)


@app.route('/secrets')
def secrets():
    if 'user_id' in session:
        user_id=session['user_id']
        user= User.query.get(user_id)
        
        return render_template('secrets.html', name=user.name)
        
    flash("You must log in to access this page", "error")
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    pass

@app.route('/success')
def success():
    return render_template("success.html")

@app.route('/download')
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
