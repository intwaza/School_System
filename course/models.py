from django.db import models

class Course(models.Model):
    course_name= models.CharField(
        max_length=20
    )
    course_trainer= models.CharField(
        max_length=12
    )
    course_code= models.CharField(
        max_length=12
    )
    course_description= models.FileField(upload_to='documents/')
    course_duration= models.PositiveSmallIntegerField()
    syllabus= models.TextField(
        max_length=700
    )

