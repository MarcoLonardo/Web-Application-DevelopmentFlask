from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app(config_class_name):
    """
    Initialise the Flask application.
    :rtype: Returns a configured Flask object
    """
    app = Flask(__name__)
    app.config.from_object(config_class_name)

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    csrf.init_app(app)
    csrf._exempt_views.add('dash.dash.dispatch')

    with app.app_context():
        # Import Dash Application
        from dash_app.dashb_app import init_dashboard
        app = init_dashboard(app)

        from my_app.models import User
        db.create_all()

    from my_app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from my_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app
