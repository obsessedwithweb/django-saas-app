from django.urls import path
from .views import register, my_view
urlpatterns = [
    path("register", register, name='regiser'),
    path("login2", my_view, name="login"),

]
