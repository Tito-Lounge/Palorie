from django.urls import path
from prompt import views

urlpatterns = [
    path("", views.home, name="home"),
    path('newEntry/', views.newEntry, name="newEntry"),
    path('error/', views.error, name='error'),
    path('process_form/', views.process_form, name='process_form'),
    path('downloadFile/', views.downloadFile, name='downloadFile'),
]
