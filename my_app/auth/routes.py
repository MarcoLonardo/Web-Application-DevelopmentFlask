from flask import Blueprint, render_template, flash, redirect, url_for
from sqlalchemy.exc import IntegrityError

from my_app import db
from my_app.auth.forms import SignupForm, LoginForm

# Setting a blueprint to authenticate users to their profile
from my_app.models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data)
        user.set_password(form.password.data)
        try:
            db.session.add(user)
            db.session.commit()
            flash(f"Hello, {user.first_name} {user.last_name}. You are signed up.")
        except IntegrityError:
            db.session.rollback()
            flash(f'Error, unable to register {form.email.data}. ', 'error')
            return redirect(url_for('auth.signup'))
        return redirect(url_for('main.index'))
    return render_template('signup.html', title='Sign Up', form=form)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    form1 = LoginForm()
    if form1.validate_on_submit():
        email = form1.email.data
        flash(f"Hello, {email}. You are logged into your account")
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Log in', form=form1)