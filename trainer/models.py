from django.db import models

class Trainer(models.Model):
    first_name= models.CharField(
        max_length=12, null=False
    )
    last_name = models.CharField(
        max_length=12, null=False
    )
    age = models.PositiveSmallIntegerField(null=False)
    gender_choice=(
        ('1','Female'),
        ('2','male'),
        ('3','none')
    )
    gender = models.CharField(
        max_length=8, choices=gender_choice, null=False
    )
    bio= models.TextField(
        max_length=700, null=False
    )
    email_address= models.EmailField(null=False)
    phone_number = models.CharField(
        max_length=12, null=False
    )
    salary= models.PositiveBigIntegerField(null=False)
    profile= models.ImageField(upload_to ='images/', null=False)
    contract= models.FileField(upload_to='documents/', null=False)
    date_hired= models.DateField(null=False)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"