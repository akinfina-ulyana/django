import logging

from profiles.forms import LoginForm, RegisterForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

logger = logging.getLogger(__name__)


def profiles(request):
    if request.GET.get("param"):
        logger.info(f"My param = {request.GET.get('param')}")
    return HttpResponse("Profiles view")


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
            )
            user.set_password(form.cleaned_data["password"])
            user.save()
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                email=form.cleaned_data["email"],
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )

            if user is None:
                return HttpResponse("BadRequest", status=400)
            login(request, user)
            return redirect("index")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("index")


# import logging
# from django.http import HttpResponse
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
#
# from profiles.forms import RegisterForm
#
# logger = logging.getLogger(__name__)
#
#
# def profiles(request):
#     if request.GET.get("param"):
#         logger.info(f"My param = {request.GET.get('param')}")
#     return HttpResponse("Shop profiles")
#
#
#
# def register(request):
#     # form = RegisterForm()
#     # return render(request, "register.html", {"form": form})
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             User.object.create()
#             logger.info(f"User email: {form.cleaned_data['email']}")
#             logger.info(f"User password: {form.cleaned_data['password']}")
#
#             return redirect("/")
#     else:
#         form = RegisterForm()
#     return render(request, "register.html", {"form":form})
#
#
