from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
# Create your views here.


class LoginTemplateView(TemplateView):
    template_name = "authenticate/login.html"


def my_view(request):
    template_name = "authenticate/login.html"

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect("/")
    return render(request, template_name)
