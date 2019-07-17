# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task, current_task
from datetime import datetime
from django_celery_results.models import TaskResult
from home.network_scanner_module.network_scanning import network_scan
from home.models import Host,Scan


@shared_task
def get_time():
    print(current_task.request)
    return datetime.now()

@shared_task
def scan_net(scan_id,scan_target,subnet,hostname=False):
    scan = Scan.objects.get(id=scan_id)
    scan_results = network_scan(scan_target,str(subnet))
    for key,value in scan_results.items():
        if value is True:
            scan.host_set.create(ip_address=key)
    


@shared_task
def update_status():
    tasks = TaskResult.objects.all()
    for task in tasks:
        if task.status != "SUCCESS":
            pass  