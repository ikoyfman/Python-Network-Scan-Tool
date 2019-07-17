from django.shortcuts import render, redirect
from home.forms import ScanForm
from home.models import Scan
from home.tasks import get_time, scan_net

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
            scan.save()
            return redirect('home')
        
        return render(request,'home/home.html',context={
            'scan_form':scan_form
        })