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

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin, db.Model):
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
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField('Sign me up')

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=["GET", "POST"])
def register():
    form = UserRegister()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            flash('Email already exists. Please choose another one or login with this one')
            return redirect(url_for('register'))

        new_user = User(
            name = form.name.data,
            email = form.email.data,
            password = generate_password_hash(form.password.data, salt_length=8)
        )

        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully!')
        return redirect(url_for('login'))
    return render_template("register.html", form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form=UserLogInForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("Login successful", "success")
            return redirect(url_for('secrets'))
        else:
            flash("Invalid email or password", "error")

    return render_template("login.html", form=form)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/secrets')
@login_required
def secrets():
    return render_template('secrets.html')

@login_manager.unauthorized_handler
def unauthorized():
    flash("You must log in to access this page", "error")
    return redirect(url_for('login'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('home'))

@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files', 'cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True)
