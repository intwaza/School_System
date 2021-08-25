from django.shortcuts import redirect, render
from .forms import TrainerRegistrationForm
from django.shortcuts import render
from .models import Trainer


def register_trainer(request):
    if request.method=="POST":
        form = TrainerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('register_trainer')
        else:
            print(form.errors)
    else:
        form= TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})

def trainer_list(request):
    trainers= Trainer.objects.all()
    return render(request,"trainer_list.html", {"trainers": trainers})
