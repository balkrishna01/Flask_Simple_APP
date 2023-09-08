from flask import Blueprint, render_template, request, flash, redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, logout_user, current_user, login_required

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
            else:
                flash('Incorrect Password or Email!', category='error')

    return render_template("login.html")


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get(('password2'))

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exits.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(fname) < 2:
            flash('First Name must be greater that one character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, fname=fname, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account Created!.', category='success')
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
            # add the user details

    return render_template("sign_up.html")
