
""" all route names"""
from datetime import datetime
from flask import render_template

from datetime import datetime
from flask import render_template, url_for, flash, redirect, request,abort
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func
from Quality import app



from Quality.models import User
from flask_mail import Message



@app.route("/")
@app.route("/home")
def home():
    """Route to display all tasks on the home page."""
    return render_template('home.html')

@app.route("/about")
def about():
    """Route to display the about page."""
    return render_template('about.html', title='About')



@app.route("/register", methods=['GET', 'POST'])
def register():
    """Route to handle user registration."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationUserForm()
    if form.validate_on_submit():
        hashed_pwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data.lower(), password=hashed_pwd)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    """Route to handle user login."""
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data.lower()).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user, remember=form.remember.data)

            current_user.last_login = datetime.utcnow()
            db.session.add(current_user)
            db.session.commit()

            flash('Login successful.', 'success')
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    """Route to handle user logout."""
    current_user.last_login = datetime.utcnow()
    db.session.add(current_user)
    db.session.commit()
    logout_user()
    return redirect(url_for('home'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """Route to handle account updates."""
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data

        current_user.last_login = datetime.utcnow()
        db.session.add(current_user)
        db.session.commit()

        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        if current_user.is_authenticated:
            form.username.data = current_user.username
            form.email.data = current_user.email
    return render_template('account.html', title='Account', form=form)
