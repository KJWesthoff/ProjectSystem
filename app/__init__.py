from flask import Flask
from app.api.routes import api
from app.api.db import init_db



def create_app(test_config= None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(SECRET_KEY = "super_secret_key")
    
    @app.route('/hello')
    def hello():
        return "hello world"

    app.register_blueprint(api)
    
    init_db(app)    
    
    return app
