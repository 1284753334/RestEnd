import os

from celery import Celery

# 指定settings 模块
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RESTEnd.settings')

app = Celery('RESTEnd')
# 从settings 中 获取配置信息
app.config_from_object('django.conf:settings', namespace='CELERY')

# 自动加载任务
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))












