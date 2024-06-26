
from django.db import models

# Create your models here.
from django.db import models

class HardwareInfo(models.Model):
    date = models.DateField()
    process_total = models.IntegerField()
    cpu_status = models.FloatField(max_length=20)
    memory_status = models.FloatField(max_length=20)
    gpu_status = models.FloatField(max_length=20)

class Device(models.Model):
    device_type = models.CharField(max_length=10)
    switch_status = models.BooleanField(default=False)
    operational_status = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.device_type