from django.shortcuts import render
from .models import VisitPage


def homepage(request, *args, **kwargs):
    template_file = "visits/home.html"
    query = VisitPage.objects.filter(path=request.path)
    my_context = {
        "visits": query
    }
    VisitPage.objects.create(path=request.path)
    return render(request, template_name=template_file, context=my_context)
