from rq.decorators import job
from stream_framework import settings
from stream_framework.storage.redis.connection import get_redis_connection


class RQTask(object):
    def __init__(self, queue='default'):
        conn = get_redis_connection('rq')
        self.wrapper = job(queue=queue, connection=conn)

    def __call__(self, f):
        return self.wrapper(f)
