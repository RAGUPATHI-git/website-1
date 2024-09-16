from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return "log in"

@auth.route('/logout')
def logout():
    return "log out"

@auth.route('/sign-up')
def sign_up():
    return "sign up"

