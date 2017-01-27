import os
from flask import Flask
from flask_jsglue import JSGlue
from flask_login import LoginManager
from flask_security import SQLAlchemyUserDatastore, Security
from flask_sqlalchemy import SQLAlchemy
from config import basedir
from app import custom_filters

import logging
from logging.handlers import TimedRotatingFileHandler

app = Flask(__name__,
            template_folder=os.path.join(basedir, 'app', 'templates'),
            static_folder=os.path.join(basedir, 'app', 'static'))
app.config.from_object('config')
app.register_blueprint(custom_filters.blueprint)

file_handler = TimedRotatingFileHandler(app.config['ACCESS_LOG'], when='d')
logger = logging.getLogger('werkzeug')
logger.handlers = [file_handler]
logger.propagate = False

app.logger.handlers = [file_handler]
app.logger.propagate = False

jsglue = JSGlue(app)

login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

from app.models import List, Item, User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

