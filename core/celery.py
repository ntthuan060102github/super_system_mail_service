import os
from celery import Celery

from pkg_helpers.services.queue_name import MAIL_QUEUE

# celery -A core worker -l info --autoscale 3,10

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery(MAIL_QUEUE)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.task_default_queue = MAIL_QUEUE