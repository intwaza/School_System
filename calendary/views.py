from django.http.response import HttpResponseRedirect
from .forms import EventForm
from django.shortcuts import get_object_or_404, redirect, render

from datetime import date, datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils.safestring import mark_safe

from .models import Event
from .utils import Calendar

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        calendar = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = calendar.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()
def event(request, event_id=None):
    instance= Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reversed('cal:calendar'))
    return render(request, 'calendary/event.html', {'form': form})

def event_form(request):
    if request.method=="POST":
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_form')
        else:
            print(form.errors)
    else:
        form= EventForm()
    return render(request,"event_form.html",{"form":form})
# Create your views here.
