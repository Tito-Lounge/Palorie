from django.urls import path
from prompt import views

urlpatterns = [
    path("", views.home, name="home"),
]
