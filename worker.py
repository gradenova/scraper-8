import os
from dateutil.tz import gettz
from dateutil.parser import parse
from datetime import timedelta, datetime

import redis
from rq import Queue, Connection
from rq_scheduler import Scheduler

from scraper import scraper

if os.getenv('DEBUG'):
    from rq import Worker
else:
    from rq.worker import HerokuWorker as Worker


TIME_ZONE = gettz(os.getenv('TIME_ZONE', 'America/Atlanta'))
RUN_AT = parse(os.getenv('RUN_AT', '17:15'), tzinfos=TIME_ZONE)

listen = ['default']

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')

if not redis_url:
    raise RuntimeError('Set up Redis To Go first.')

conn = redis.from_url(redis_url)

scheduler = Scheduler(connection=conn, interval=86400)


def test():
    print('Hello world, sample tasks.')


if __name__ == '__main__':

    scheduler.enqueue_in(timedelta(seconds=5), test)

    scheduler.schedule(
        scheduled_time=datetime.utcnow(),
        func=scraper,
        interval=86400,
        description='Scraper Job'
    )

    with Connection(conn):
        worker = Worker(map(Queue, listen))
        scheduler.run()
        worker.work()
