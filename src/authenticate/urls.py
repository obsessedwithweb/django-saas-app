from django.urls import path
from .views import LoginTemplateView, my_view
urlpatterns = [
    path("login", LoginTemplateView.as_view()),
    path("login2", my_view),

]
