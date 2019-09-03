from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exceptioinTest.settings')
app = Celery('exceptioinTest')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def save_exception(self, exception_type, exception_string, exception_repr, exception_args, exception_traceback):
    from main.models import Main
    main = Main(exception_type=exception_type, exception_string=exception_string, exception_repr=exception_repr, exception_args=exception_args, exception_traceback=exception_traceback)
    main.save()
    print(exception)
