from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Homework, Classes
from .forms import Create_Homework, Create_Class

# Create your views here.
def frontpage(request):
    return render(request, "frontpage.html")

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("frontpage")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def signup_view(request):
    if request.method == "POST":   
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("frontpage")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})

def create_homework(request):
    if request.method == "POST":
        form = Create_Homework(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homework")
    else:
        form = Create_Homework()
    return render(request, "create_homework.html", {"form": form})

def homework(request):
    homework = Homework.objects.all()
    return render(request, "homework.html", {"homeworks": homework})

def add_class(request):
    if request.method == "POST":
        form = Create_Class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("classes")
    else:
        form = Create_Class()
    return render(request, "add_class.html", {"form": form})

def classes(request):
    classest = Classes.objects.all()
    return render(request, "classes.html", {"classes": classest})