from django.db import models
from django.urls import reverse

class Event(models.Model):
    event_name= models.CharField(
        max_length=15, null=False
    )
    event_task= models.TextField(
        max_length=80, null= False
    )
    event_duration= models.TimeField(null=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)

    def __str__(self):
        return self.event_name


    @property
    def get_html_url(self):
        url = reverse('calendary:event_edit', args=(self.id,))
        return f'<p>{self.event_name}</p><a href="{url}">edit</a>'