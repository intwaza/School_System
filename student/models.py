from django.db import models
from datetime import datetime
import datetime

from django.urls.base import reverse

class Student(models.Model):
    first_name = models.CharField(
        max_length=12, default='SOME STRING'
    )
    last_name = models.CharField(
        max_length=12, default='SOME STRING'
    )
    age = models.PositiveSmallIntegerField(default= 19)
    date_of_birth = models.DateField(null= True)
    national_id= models.CharField(
        max_length= 20, null=True
    )
    profile = models.ImageField(upload_to ='images/',null=True)
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
    date_of_enrollment = models.DateTimeField(null=True)
    

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
        max_length=10,blank=True,null=False, default=1
    )
    def test_register(self):  
        url=reverse('register_course')
        data={
            "course_code":self.course.course_code,
            "course_name":self.course.course_name,
            "course_trainer":self.course.course_trainer,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
    
    def test_courses_list_view(self):
        url=reverse('courses_list')
        data={
            "course_code":self.course.course_code,
            "course_name":self.course.course_name,
            "course_trainer":self.course.course_trainer,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)
        