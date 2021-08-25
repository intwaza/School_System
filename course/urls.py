from django.conf.urls import url
from django.urls import path
from .views import course_form, course_list

urlpatterns=[
    path("register", course_form, name="course_form"),
    path("list/", course_list, name="course_list")
]