""" comments """
from flask import Blueprint


auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    """Route to display login page."""
    return "<h1>Login</h1>"


@auth.route('/logout')
def logout():
    """Route to display logout page."""
    return "<h1>Logout</h1>"

@auth.route('/sign-up')
def register():
    """Route to display signup page."""
    return "<h1>Register</h1>"
