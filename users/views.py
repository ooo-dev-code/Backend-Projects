from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from store.models import Bank_account

# Create your views here.
def frontpage(request):
    return render(request, "frontpage.html")

def login_(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("frontpage")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def signup(request):
    if request.method == "POST":   
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("frontpage")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})