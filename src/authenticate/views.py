from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
# from django.views.generic import TemplateView
# Create your views here.



def my_view(request):
    template_name = "authenticate/login.html"
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            print("user ", user)
            if user is not None:
                login(request, user)
                return redirect("/")
    return render(request, template_name)


def register(request):
    template_name = "authenticate/register.html"
    User = get_user_model()
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST['password']
        try:
            User.objects.create_user(username,email, password)
        except:
            pass
        return redirect("home")
    return render(request, template_name)
