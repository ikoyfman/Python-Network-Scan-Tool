from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from home.forms import ScanForm
from home.models import Scan, Host
from home.tasks import get_time, scan_net, scan_host_ports

# Create your views here.
def home(request):
    if request.method == 'GET':
        
        scans = Scan.objects.all()
        scan_form = ScanForm()
        return render(request,'home/home.html',context={
            'scan_form':scan_form,
            'scans':scans,
        })
    if request.method == 'POST':
        scan_form = ScanForm(request.POST)
        if scan_form.is_valid():
            scan = scan_form.save()
            scan.scan_name = (scan.scan_target + " " + scan.start_time.strftime("%D %H:%M"))
            scan_net_task = scan_net.delay(scan.id,scan.scan_target,scan.subnet)
            scan.task_id = scan_net_task.id
            scan.status = "In Progress"
            scan.save()
            return redirect('home')
        
        return render(request,'home/home.html',context={
            'scan_form':scan_form
        })

def results(request, scan_id):
    if request.method == 'GET':
        scan = Scan.objects.get(id=scan_id)
        host_results = get_list_or_404(scan.host_set)
        data = {
            'host_results':host_results,
            'scan':scan,
            }
        return render(request, 'home/results.html', data)

    if request.method == "POST":
        scan = Scan.objects.get(id=scan_id)
        results = get_list_or_404(scan.host_set)
        host_list = []
        for host in results:
            host_list.append(host.ip_address)
        scan_results = scan_host_ports.delay(host_list)
                           
        