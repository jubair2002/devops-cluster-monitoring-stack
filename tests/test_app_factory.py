import pytest
from backend.app import create_app
from backend.config import Config


def test_app_creation():
    """Test that the app factory creates an app instance"""
    app = create_app(Config)
    assert app is not None
    assert app.config['TESTING'] is False


def test_app_config():
    """Test that app configuration is loaded correctly"""
    app = create_app(Config)
    assert 'SECRET_KEY' in app.config
    assert 'DEBUG' in app.config
    assert 'HOST' in app.config
    assert 'PORT' in app.config


def test_app_blueprint_registration():
    """Test that blueprints are registered"""
    app = create_app(Config)
    assert 'main' in [bp.name for bp in app.blueprints.values()]

