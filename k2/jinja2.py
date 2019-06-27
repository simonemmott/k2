from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment
import random

def secret(length=30):
    return ''.join(random.choice('abcdefghighjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(length))

def environment(**options):
    options['trim_blocks'] = options.get('trim_blocks', True)
    options['lstrip_blocks'] = options.get('lstrip_blocks', True)
    env = Environment(**options)
    env.globals.update({
        'static': staticfiles_storage.url,
        'url': reverse,
        'secret': secret,
    })
    return env