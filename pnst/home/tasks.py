# Create your tasks here
from __future__ import absolute_import, unicode_literals
from celery import shared_task, current_task
from datetime import datetime
from django_celery_results.models import TaskResult
from home.network_scanner_module.network_scanning import network_scan
from home.network_scanner_module.port_scanner_threading import scan_ports
from home.models import Host,Scan


@shared_task
def get_time():
    print(current_task.request)
    return datetime.now()

@shared_task
def scan_net(scan_id,scan_target,subnet,hostname=False):
    scan = Scan.objects.get(id=scan_id)
    if not scan.subnet:
        scan_results = network_scan(scan_target,"0",hostname=True)
        scan.host_set.create(ip_address=scan_target)
    else:
        scan_results = network_scan(scan_target,str(subnet))
    
        for key,value in scan_results.items():
            if value is True:
                scan.host_set.create(ip_address=key)
        
    scan.status = "Finished"
    scan.save()

@shared_task
def scan_host_ports(list_of_hosts):
    for host in list_of_hosts:
        print(host)
        result = scan_ports(host,1,1024)

    

@shared_task
def update_status():
    tasks = TaskResult.objects.all()
    for task in tasks:
        if task.status != "SUCCESS":
            pass  