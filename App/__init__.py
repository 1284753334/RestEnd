

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
#  __all__  可被外界访问的属性
from .celerymy import app as celery_app

__all__ = ('celery_app',)
