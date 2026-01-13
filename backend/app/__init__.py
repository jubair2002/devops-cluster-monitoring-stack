from flask import Flask
from backend.config import Config
import os


def create_app(config_class=Config):
    """Application factory pattern"""
    # Set template and static folders to root level
    template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../templates'))
    static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../static'))
    
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    app.config.from_object(config_class)
    
    # Register blueprints
    from backend.app.routes import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app

