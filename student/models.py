from django.db import models
from datetime import datetime

class Student(models.Model):
    first_name = models.CharField(
        max_length=12, default='SOME STRING'
    )
    last_name = models.CharField(
        max_length=12, default='SOME STRING'
    )
    age = models.PositiveSmallIntegerField(default='SOME STRING')
    date_of_birth = models.DateField(default='SOME STRING')
    national_id= models.CharField(
        max_length= 20, default='SOME STRING'
    )
    profile = models.ImageField(upload_to ='images/', default='SOME STRING')
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','South Sudanese'),
        ('5','Sudanese')
    )
   
    nationality = models.CharField(
        max_length=15, choices=nationality_choice, default='SOME STRING'
    )
    gender_choice=(
        ('1','Female'),
        ('2','male'),
        ('3','none')
    )
    gender = models.CharField(
        max_length=8, choices=gender_choice, default='SOME STRING'
    )
    guardian_name = models.CharField(
        max_length=12, default='SOME STRING'
        )
    email_address= models.EmailField(default='SOME STRING')
    district = models.CharField(
        max_length=12, default='SOME STRING'
    )
    phone_number = models.CharField(
        max_length=12, default='SOME STRING'
        
    )
    medical_report = models.FileField(upload_to='documents/', default='SOME STRING')
    date_of_enrollment = models.DateTimeField(default=datetime.now)
    

    course_name = models.CharField(
        max_length=18,
        null=False,
        default='SOME STRING'
    )
    languages_choice=(
        ('1','English'),
        ('2','Kinyarwanda'),
        ('3','French'),
        ('4','Kiswahili'),
        ('5','Luganda')
        
    )

    languages = models.CharField(
        max_length=20, choices=languages_choice, default='SOME STRING'
    )
    laptop_number = models.CharField(
        max_length=10,blank=True,null=False, default='SOME STRING'
    )
    def full_name(self):
        return f"{self.first_name} {self.last_name}"