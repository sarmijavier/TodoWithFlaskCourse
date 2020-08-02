from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from .auth import auth

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static') #se pasa por referencia el nombre de la aplicación el cual es el nombre del archivo
    bootstrap = Bootstrap(app) # la instancia de bootstrap recive una app de flask

    app.config.from_object(Config)

    app.register_blueprint(auth)

    return app