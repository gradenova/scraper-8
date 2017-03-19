from rq_scheduler import Scheduler
from datetime import datetime, timedelta


from app import app
from scraper import scraper
from worker import conn

RUN_AT = app.config.get('RUN_AT')
TIME_ZONE = app.config.get('TIME_ZONE')


scheduler = Scheduler(connection=conn)


def run():
    print('Job is scheduled')


def hello():
    print('Hello world, sample tasks.')


scheduler.schedule(
    scheduled_time=RUN_AT,
    func=scraper,
    interval=86000,
)

scheduler.enqueue_at(datetime.utcnow(), run)
scheduler.enqueue_at(timedelta(seconds=15), hello)

# scheduler.cron(
#     cron_string,                # A cron string (e.g. "0 0 * * 0")
#     func=func,                  # Function to be queued
#     args=[arg1, arg2],        # Arguments passed into function when executed
#     # Keyword arguments passed into function when executed
#     kwargs={'foo': 'bar'},
#     # Repeat this number of times (None means repeat forever)
#     repeat=10,
#     queue_name=queue_name   # In which queue the job should be put in
# )
