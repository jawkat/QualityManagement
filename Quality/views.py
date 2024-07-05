from flask import Blueprint


views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to display home page."""
    return "<h1>Home</h1>"
