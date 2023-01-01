from flask import Flask

from config import Config
from app.extensions import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    from app.tech import bp as tech_bp
    
    
    app.register_blueprint(main_bp)
    app.register_blueprint(tech_bp, url_prefix='/tech')

    return app