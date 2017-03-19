import schedule

from app import app
from scraper import scraper

RUN_AT = app.config.get('RUN_AT')

# Setup scheduler
schedule.every().day.at(RUN_AT).do(scraper)


def run():
    schedule.run()
    print('Job is scheduled')
