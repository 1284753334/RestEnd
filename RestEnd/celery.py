import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
#  后加项目名
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RestEnd.settings')
#  后加项目名
app = Celery('RestEnd')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))








