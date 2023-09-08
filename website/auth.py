from flask import Blueprint, render_template, request, flash, redirect,url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html")


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<p> Logout <p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get(('password2'))

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
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
            return redirect(url_for('views.home'))
            # add the user details

    return render_template("sign_up.html")
