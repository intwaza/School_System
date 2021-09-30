from django.db import models

class Course(models.Model):
    course_name= models.CharField(
        max_length=20, default='SOME STRING'
    )
    course_trainer= models.CharField(
        max_length=12, default='SOME STRING'
    )
    course_code= models.CharField(
        max_length=12, default=0
    )
    course_description= models.FileField(upload_to='documents/', null=True)
    course_duration= models.PositiveSmallIntegerField(default=0)
    syllabus= models.TextField(
        max_length=700, null=True
    )

