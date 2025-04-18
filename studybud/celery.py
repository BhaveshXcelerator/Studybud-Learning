from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studybud.settings")
app = Celery("studybud.settings")
app.conf.enable_utc = False

app.conf.update(timezone = "America/New_York")
app.config_from_object(settings, namespace="CELERY")

app.conf.beat_schedule = {
    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')