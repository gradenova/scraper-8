from rq_scheduler import Scheduler
from datetime import datetime, timedelta
from redis import Redis
from rq_scheduler import Scheduler
from app import app, rq
from scraper import scraper

from rq_scheduler import Scheduler
from datetime import timedelta, datetime

from scraper import scraper
from scheduler import run_t, test

# Get a scheduler for the "default" queue
scheduler = Scheduler(connection=Redis())

# Puts a job into the scheduler. The API is similar to RQ except that it
# takes a datetime object as first argument. So for example to schedule a

RUN_AT = app.config.get('RUN_AT')
TIME_ZONE = app.config.get('TIME_ZONE')

scheduler = Scheduler(connection=conn)


@rq.job('low', timeout=180, ttl=60 * 60 * 24)
def run():
    print('Job is scheduled')


@rq.job
def hello():
    print('Hello world, sample tasks.')


hello.schedule(timedelta(seconds=60))

RUN_AT = app.config.get('RUN_AT')
TIME_ZONE = app.config.get('TIME_ZONE')

scheduler.schedule(
    scheduled_time=RUN_AT,
    func=scraper,
    interval=86000,
)

scheduler.enqueue_in(datetime.utcnow(), run_t)
scheduler.enqueue_in(timedelta(seconds=15), test)

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

# job to run on Jan 1st 2020 we do:
scheduler.enqueue_at(datetime(2020, 1, 1), run)  # Date time should be in UTC

# Here's another example scheduling a job to run at a specific date and time (in UTC),
# complete with args and kwargs.
scheduler.enqueue_at(datetime(2020, 1, 1, 3, 4), func, foo, bar=baz)
