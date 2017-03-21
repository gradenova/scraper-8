import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import rq_dashboard

from rq import Queue
from rq.job import Job

from worker import conn
from utils import add_basic_auth

app = Flask(__name__)

db = SQLAlchemy(app)

app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))

q = Queue(connection=conn)

if not app.config.get('TESTING'):
    add_basic_auth(rq_dashboard.blueprint,
                   os.getenv('USER', 'admin'), os.getenv('PASSWORD', '[]'))

app.register_blueprint(rq_dashboard.blueprint, url_prefix='/monitor')


def test():
    print('sknsjkfnknk')
    return 'Hello world, sample tasks.'


@app.route('/')
def hello():
    return 'Nothing to see here. :)'


if __name__ == '__main__':
    from scraper import scraper
    job = q.enqueue_call(func=test, result_ttl=5000)
    print(job.id)
    app.run()
