from django.db import models
from django.urls import reverse

class Event(models.Model):
    event_name= models.CharField(
        max_length=15, default=' SOME STRING'
    )
    event_task= models.TextField(
        max_length=80, default= 'SOME STRING'
    )
    event_duration= models.TimeField(default='SOME STRING')
    start_time = models.DateTimeField(default= 'SOME STRING')
    end_time = models.DateTimeField(default= 'SOME STRING')

    def __str__(self):
        return self.event_name


    @property
    def get_html_url(self):
        url = reverse('calendary:event_edit', args=(self.id,))
        return f'<p>{self.event_name}</p><a href="{url}">edit</a>'