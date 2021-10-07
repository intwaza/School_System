from django.conf.urls import url
from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.student= Student(first_name= "Belyse",
                               last_name= "Intwaza", 
                                age= 20, 
                                gender="Female", 
                                guardian_name="Intwaza",
                                district="Kicukiro",
                                email_address="iintwazabelyse@gmail.com",
                                phone_number="0439942043"
                                )
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name, self.student.full_name())
    
    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name, self.student.full_name())
    
    def test_student_year_of_birth(self):
        current_year= datetime.datetime.now().year
        year= current_year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())
    
    def test_register_student_view(self):
        url= reverse('register_student')
        data={
            "first_name": self.student.first_name,
            "last_name": self.student.last_name,
            "age": self.student.age,
            "gender":self.student.gender,
            "guardian_name":self.student.guardian_name,
            "district": self.student.district,
            "email_address": self.student.email_address,
            "phone_number":self.student.phone_number,
            }
        request= self.client.post(url,data)
        self.assertEqual(request.status_code,200)