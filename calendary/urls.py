from django.urls  import path
from . import views
from .views import event_form
urlpatterns=[
      path("calendar/", views.CalendarView.as_view() , name='calendar'),
      path("events/", views.event, name='event'),
      path("list/", event_form, name="student_list")
      # path("calendary/", get_date, name='get_date')

]