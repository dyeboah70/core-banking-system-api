from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core_banking_api.settings")

app = Celery("core_banking_api")
app.conf.enable_utc = False
app.conf.broker_connection_retry_on_startup = True
app.conf.update(timezone="Africa/Accra")

app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'calculate_interest': {
        'task': 'calculate_interest',
        # http://docs.celeryproject.org/en/latest/userguide/periodic-tasks.html
        'schedule': crontab(0, 0, day_of_month='1'),
    }
}


@app.task(bind=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
