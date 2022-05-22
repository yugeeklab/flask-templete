from flask import Flask
from .extensions import bcrypt, cors, db, jwt, ma, migrate

def create_app(config_name):
    from config import config_by_name
    from app.apiv1 import blueprint as api1
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])
    register_extensions(app)
    app.register_blueprint(api1, url_prefix='/api/v1')
    
    return app

def register_extensions(app):
    # Registers flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    cors.init_app(app)