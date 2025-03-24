from flask import Flask
from app.routes import api_bp
from app.db import init_db

def create_app():
    app = Flask(__name__)

    init_db(app)
    from app.routes import api_bp  
    app.register_blueprint(api_bp)

    return app
