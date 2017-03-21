import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import rq_dashboard
from utils import add_basic_auth

app = Flask(__name__)

app.config.from_object(os.getenv('APP_SETTINGS', 'config.DevelopmentConfig'))

db = SQLAlchemy(app)

if not app.config.get('TESTING'):
    add_basic_auth(rq_dashboard.blueprint,
                   os.getenv('USER', 'admin'), os.getenv('PASSWORD', '[]'))

app.register_blueprint(rq_dashboard.blueprint, url_prefix='/monitor')


def test():
    print('Hello world, sample tasks.')


@app.route('/')
def hello():
    return 'Nothing to see here. :)'


if __name__ == '__main__':
    from worker import scheduler
    from datetime import timedelta, datetime

    from scraper import scraper

    scheduler.enqueue_in(timedelta(seconds=5), test)

    scheduler.schedule(
        scheduled_time=datetime.utcnow(),
        func=scraper,
        interval=86400,
        description='Scraper Job'
    )

    scheduler.run()
    app.run()
