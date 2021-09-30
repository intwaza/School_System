from django.db import models

class Trainer(models.Model):
    first_name= models.CharField(
        max_length=12, default='SOME STRING'
    )
    last_name = models.CharField(
        max_length=12, default='SOME STRING'
    )
    age = models.PositiveSmallIntegerField(default=25)
    gender_choice=(
        ('1','Female'),
        ('2','male'),
        ('3','none')
    )
    gender = models.CharField(
        max_length=8, choices=gender_choice, default='SOME STRING'
    )
    bio= models.TextField(
        max_length=700, default='SOME STRING'
    )
    email_address= models.EmailField(default='SOME STRING')
    phone_number = models.CharField(
        max_length=12, default='SOME STRING'
    )
    salary= models.PositiveBigIntegerField(default=400)
    profile= models.ImageField(upload_to ='images/', null=True)
    contract= models.FileField(upload_to='documents/', null=True)
    date_hired= models.DateField(null=True)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"