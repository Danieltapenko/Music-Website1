from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


website = Flask(__name__)
website.config.from_object(Config)
db = SQLAlchemy(website)
migrate = Migrate(website,db)
login = LoginManager(website)
#mail = Mail(website)

from app import routes,forms,mail,models