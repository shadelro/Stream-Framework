from stream_framework import settings
from stream_framework.utils import get_class_from_string


class task(object):
    wrapper_cls = get_class_from_string(settings.STREAM_ASYNC_CLASS)

    def __init__(self, *args, **kwargs):
        self.wrapper = self.wrapper_cls(*args, **kwargs)

    def __call__(self, f):
        return self.wrapper(f)
