from django.urls import path
from prompt import views

urlpatterns = [
    path("", views.home, name="home"),
    path('error/', views.error, name='error'),
    path('process_form/', views.process_form, name='process_form'),
    path('downloadFile/', views.downloadFile, name='downloadFile'),
    path('entry_list/', views.entry_list, name='entry_list'),
    path('entry_detail/<str:filename>/', views.entry_detail, name='entry_detail'),
    path('csv/<str:filename>/download', views.download_file, name='download_file'),
]
