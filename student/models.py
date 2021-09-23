from django.db import models
from datetime import datetime

class Student(models.Model):
    first_name = models.CharField(
        max_length=12
    )
    last_name = models.CharField(
        max_length=12
    )
    age = models.PositiveSmallIntegerField()
    date_of_birth = models.DateField()
    national_id= models.CharField(
        max_length= 20
    )
    profile = models.ImageField(upload_to ='images/')
    nationality_choice=(
        ('1','Rwandan'),
        ('2','Kenyan'),
        ('3','Ugandan'),
        ('4','South Sudanese'),
        ('5','Sudanese')
    )
   
    nationality = models.CharField(
        max_length=15, choices=nationality_choice
    )
    gender_choice=(
        ('1','Female'),
        ('2','male'),
        ('3','none')
    )
    gender = models.CharField(
        max_length=8, choices=gender_choice
    )
    guardian_name = models.CharField(
        max_length=12
        )
    email_address= models.EmailField()
    district = models.CharField(
        max_length=12
    )
    phone_number = models.CharField(
        max_length=12,
        
    )
    medical_report = models.FileField(upload_to='documents/')
    date_of_enrollment = models.DateTimeField(default=datetime.now)
    

    course_name = models.CharField(
        max_length=18,
        null=False
    )
    languages_choice=(
        ('1','English'),
        ('2','Kinyarwanda'),
        ('3','French'),
        ('4','Kiswahili'),
        ('5','Luganda')
        
    )

    languages = models.CharField(
        max_length=20, choices=languages_choice
    )
    laptop_number = models.CharField(
        max_length=10,blank=True,null=True
    )
    def full_name(self):
        return f"{self.first_name} {self.last_name}"