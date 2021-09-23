from django.db import models

class Course(models.Model):
    course_name= models.CharField(
        max_length=20, null=False
    )
    course_trainer= models.CharField(
        max_length=12, null=False
    )
    course_code= models.CharField(
        max_length=12, null=False
    )
    course_description= models.FileField(upload_to='documents/', null=False)
    course_duration= models.PositiveSmallIntegerField(null=False)
    syllabus= models.TextField(
        max_length=700, null=False
    )

