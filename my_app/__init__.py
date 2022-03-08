from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)

    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    csrf._exempt_views.add('dash.dash.dispatch')

    with app.app_context():
        # Import Dash Application
        from dash_app.dashb_app import init_dashboard
        app = init_dashboard(app)

    return app
