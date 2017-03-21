import os
import redis
from rq import Queue, Connection
from rq.worker import HerokuWorker as Worker


listen = ['high', 'default', 'low']

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')

if not redis_url:
    raise RuntimeError('Set up Redis To Go first.')

conn = redis.from_url(redis_url)


if __name__ == '__main__':

    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()
