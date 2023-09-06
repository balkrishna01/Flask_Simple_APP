from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")


@auth.route('/logout', methods=['GET', 'POST'])
def logout():
    return "<p> Logout <p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get(('password2'))

        if len(email) < 4:
            pass
        elif len(firstName):
            pass
        elif password1 != password2:
            pass
        elif len(password1) < 7:
            pass
        else:
            #add the user details

    return render_template("sign_up.html")
