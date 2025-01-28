from django.shortcuts import render
# from django.contrib.auth.decorators import login_required  # ~ FBVs
from django.contrib.admin.views.decorators import staff_member_required  # ~ FBVs
# from django.contrib.auth.mixins import LoginRequiredMixin  # ~ CBVs
from django.views.generic import View
from django.conf import settings
from .models import VisitPage

LOGIN_URL = settings.LOGIN_URL

def homepage(request, *args, **kwargs):
    template_file = "visits/home.html"
    query = VisitPage.objects.filter(path=request.path)
    my_context = {
        "visits": query.order_by('timestamp')[:5],
        "auth": request.user.is_authenticated
    }
    VisitPage.objects.create(path=request.path)
    return render(request, template_name=template_file, context=my_context)


# class AboutView(LoginRequiredMixin, View):
#     def get(self, request):
#         template_name = "visits/about.html"
#         return render(request, template_name)

@staff_member_required(login_url=LOGIN_URL)
def about(request):
    template_name = "visits/about.html"
    return render(request, template_name)
