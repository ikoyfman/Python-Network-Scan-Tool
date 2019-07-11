from django.shortcuts import render, redirect
from home.forms import ScanForm


# Create your views here.
def home(request):
    if request.method == 'GET':
        scan_form = ScanForm()
        return render(request,'home/home.html',context={
            'scan_form':scan_form
        })
    if request.method == 'POST':
        scan_form = ScanForm(request.POST)
        if scan_form.is_valid():
            scan = scan_form.save()
            scan.scan_name = (scan.scan_target + " " + scan.start_time.strftime("%D %H:%M"))
            scan.save()
            return redirect('home')
        
        return render(request,'home/home.html',context={
            'scan_form':scan_form
        })