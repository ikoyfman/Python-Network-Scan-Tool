from django.contrib import admin
from .models import Scan, Host

# Register your models here.
@admin.register(Scan)
class ScanAdmin(admin.ModelAdmin):
    list_display = ('id', 'scan_name', 'start_time', 'end_time', 'scan_target', 'subnet','status')

@admin.register(Host)
class Host(admin.ModelAdmin):
    list_display = ('ip_address','scan_id')