from flask import Blueprint, render_template


views = Blueprint('views', __name__)


@views.route('/')
def home():
    """Route to display home page."""
    return render_template('home.html')
