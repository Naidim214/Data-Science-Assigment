"""47.Describe the steps to create a Flask blueprint and why you might use one."""
from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

@auth_bp.route('/login')
def login():
    return "Login Page"

from flask import Flask
app = Flask(__name__)
app.register_blueprint(auth_bp)


if __name__=="__main__":
    app.run()