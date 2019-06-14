from celery import shared_task


class CeleryTask(object):
    def __call__(self, f):
        return shared_task(f)
