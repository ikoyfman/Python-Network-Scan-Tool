# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task, current_task
from datetime import datetime


@shared_task
def get_time():
    print(current_task.request)
    return datetime.now()