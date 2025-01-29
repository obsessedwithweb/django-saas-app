from django.shortcuts import render, get_object_or_404
# from django.http.response import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# from django.views.generic import TemplateView
User = get_user_model()

@login_required
def user_profile(request, username: str):
    template_name = "profiles/profile.html"
    # profile_user = get_user_model().objects.get(username=username)
    profile_user = get_object_or_404(User, username=username)
    user = request.user
    if user != profile_user:
      return render(request, "404.html")
    return render(request, template_name=template_name)
