from django.db import models

class Trainer(models.Model):
    first_name= models.CharField(
        max_length=12
    )
    last_name = models.CharField(
        max_length=12
    )
    age = models.PositiveSmallIntegerField()
    gender_choice=(
        ('1','Female'),
        ('2','male'),
        ('3','none')
    )
    gender = models.CharField(
        max_length=8, choices=gender_choice
    )
    bio= models.TextField(
        max_length=700
    )
    email_address= models.EmailField()
    phone_number = models.CharField(
        max_length=12
    )
    salary= models.PositiveBigIntegerField()
    profile= models.ImageField(upload_to ='images/')
    contract= models.FileField(upload_to='documents/')
    date_hired= models.DateField()
    def full_name(self):
        return f"{self.first_name} {self.last_name}"