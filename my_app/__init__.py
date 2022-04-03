from pathlib import Path

import pandas as pd
from flask import Flask
import dash
import dash_bootstrap_components as dbc
from flask.helpers import get_root_path
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_uploads import UploadSet, IMAGES, configure_uploads

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()
photos = UploadSet('photos', IMAGES)


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
    configure_uploads(app, photos)
    csrf.exempt_views.add('dash.dash.dispatch')
    register_dashapp(app)

    with app.app_context():
        # Import Dash Application
        from my_app.models import User, Profile, Region
        db.create_all()
        add_noc_data()

    from my_app.main.routes import main_bp
    app.register_blueprint(main_bp)

    from my_app.auth.routes import auth_bp
    app.register_blueprint(auth_bp)

    return app


def add_noc_data():
    filename = Path(__file__).parent.joinpath('dash_app', 'Data', 'EU_regions.csv')
    df = pd.read_csv(filename, usecols=['region'])
    df.dropna(axis=0, inplace=True)
    df.drop_duplicates(subset=['region'], keep='first', inplace=True)
    df.reset_index(drop=True, inplace=True)
    df['id'] = df.index
    df.to_sql(name='region', con=db.engine, if_exists='replace', index=False)


def register_dashapp(app):
    from my_app.dash_app import layout
    from my_app.dash_app.callbacks import register_callbacks

    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    dashapp = dash.Dash(__name__,
                        server=app,
                        url_base_pathname='/dashboard/',
                        assets_folder=get_root_path(__name__) + '/dashboard/assets/',
                        meta_tags=[meta_viewport],
                        external_stylesheets=[dbc.themes.LUX])

    with app.app_context():
        dashapp.title = 'Dashboard'
        dashapp.layout = layout.layout
        register_callbacks(dashapp)

    _protect_dash_views(dashapp)


def _protect_dash_views(dash_app):
    for view_func in dash_app.server.view_functions:
        if view_func.startswith(dash_app.config.routes_pathname_prefix):
            dash_app.server.view_functions[view_func] = login_required(dash_app.server.view_functions[view_func])
