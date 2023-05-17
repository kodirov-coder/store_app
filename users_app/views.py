from django.contrib import auth, messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserLoginForm, UserRegisterForm, UserProfileForm
from products_app.models import Basket

def login_view(request):
    if request.method == "POST":
        form = UserLoginForm(data = request.POST)
        
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("main-page"))
    else:      
        form = UserLoginForm()
    context = {
        "form": form
    }
    return render(request, "users/login.html", context)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Siz ro'yxatdan o'tdingiz!")
            return HttpResponseRedirect(reverse("login-page"))
    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "users/register.html", context)


def profile_view(request):
    if request.method == "POST":
        user = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if user.is_valid():
            user.save()
            messages.success(request, "Malumotlar yangilandi!")
            return HttpResponseRedirect(reverse("profile-page"))
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)

    context = {
        "form": form,
        "baskets": baskets,
    }
    return render(request, "users/profile.html", context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main-page"))