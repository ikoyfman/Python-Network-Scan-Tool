from django.db import models

# Create your models here.
class Scan(models.Model):
    scan_name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    scan_target = models.CharField(max_length=50)
    subnet = models.IntegerField(blank=True, null=True)
    

class Host(models.Model):
    scan_id = models.ForeignKey(Scan, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=50)

class Open_Port(models.Model):
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE)
    port_numb = models.IntegerField()