import os
from dateutil.tz import gettz
from celery.schedules import crontab


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',
                                        'mysql://root:@localhost:3306/gfe')
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')
    BASE_URL = 'http://www.mybidmatch.com'
    QUERY_URL = '/go?sub=7F604A76-0EF9-48F1-A83F-ABC17511B6FC'
    SCRAPER_BASE_URL = BASE_URL + QUERY_URL

    TIME_ZONE = gettz(os.getenv('TIME_ZONE', 'America/Atlanta'))
    RUN_AT = os.getenv('RUN_AT', '17:15')

    RQ_POLL_INTERVAL = 5

    HOUR, MINUTE = RUN_AT.split(':')

    CELERY_BROKER_URL = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_TIMEZONE = TIME_ZONE

    CELERYBEAT_SCHEDULE = {
        'scrape-every-evening': {
            'task': 'scraper.scraper',
            'schedule': crontab(hour=HOUR, minute=MINUTE)
        }
    }


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
