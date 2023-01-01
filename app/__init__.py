from flask import Flask

from config import Config
from app.extensions import db

import logging

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # if app.config['LOG_WITH_GUNICORN']:
    #     gunicorn_error_logger = logging.getLogger('gunicorn.error')
    #     app.logger.handlers.extend(gunicorn_error_logger.handlers)
    #     app.logger.setLevel(logging.DEBUG)

    # Initialize Flask extensions
    db.init_app(app)

    # Register blueprints
    from app.main import bp as main_bp
    from app.tech import bp as tech_bp
    
    
    app.register_blueprint(main_bp)
    app.register_blueprint(tech_bp, url_prefix='/tech')

    return app