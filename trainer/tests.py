from logging import currentframe
from django.http import request
from django.test import TestCase

from trainer.views import register_trainer
from .models import Trainer
import datetime
from django.urls import reverse

class TrainerModelsTestCase(TestCase):
    def setUp(self):
        self.trainer=Trainer(first_name= "Munyivs",
        last_name="Elizabeth",
        age= 20,
        gender= "female",
        email_adress="munyivs@gmail.com",
        county="Nakuru",
        national_id="849020"
        )
    
    def test_full_name_contains_first_name(self):
        self.assertIn(self.trainer.first_name,self.trainer.full_name())

    def test_full_name_contains_last_name(self):
        self.assertIn(self.trainer.last_name,self.trainer.full_name())

    def test_trainer_year_of_birth(self):
        current_year=datetime.datetime.now().year
        year=2021 -self.trainer.age
        self.assertEqual(year,self.trainer.year_of_birth())
     
    def test_register_trainer_view(self):  
        url=reverse('register_trainer')
        data={
            "first_name":self.trainer.first_name,
            "last_name":self.trainer.last_name,
            "age":self.trainer.age,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)


    def test_trainers_list_view(self):
        url=reverse('trainers_list')
        data={
            "first_name":self.trainer.first_name,
            "last_name":self.trainer.last_name,
            "age":self.trainer.age,
            }
        request=self.client.post(url,data)
        self.assertEqual(request.status_code,200)