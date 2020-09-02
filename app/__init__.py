from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from .models import UserModel

from .config import Config
from .auth import auth


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)


def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static') #se pasa por referencia el nombre de la aplicación el cual es el nombre del archivo
    bootstrap = Bootstrap(app) # la instancia de bootstrap recive una app de flask
    login_manager.init_app(app)
    app.config.from_object(Config)

    app.register_blueprint(auth)

    return app