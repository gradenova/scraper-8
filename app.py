import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import rq_dashboard
from rq import Queue

from worker import conn
from utils import add_basic_auth

app = Flask(__name__)

db = SQLAlchemy(app)
q = Queue(connection=conn)

app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))

if not app.config.get('TESTING'):
    add_basic_auth(rq_dashboard.blueprint,
                   os.getenv('USER', 'admin'), os.getenv('PASSWORD', '[]'))

app.register_blueprint(rq_dashboard.blueprint, url_prefix='/monitor')


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
