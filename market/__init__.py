import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(app.instance_path, 'market.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'd935d2eea177cc66e70f6c72'

db = SQLAlchemy(app)

from market import routes