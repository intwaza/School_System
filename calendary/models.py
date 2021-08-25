from django.db import models
from django.urls import reverse

class Event(models.Model):
    event_name= models.CharField(
        max_length=15, null=True
    )
    event_guest= models.FileField(upload_to='documents/', null=True)
    event_task= models.TextField(
        max_length=80, null= True
    )
    event_reminder= models.FileField(upload_to='documents/', null=True)
    event_duration= models.TimeField(null=True)
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
   
