from django.urls import path
from uploadApp import views

urlpatterns = [
    path('', views.upload_file),
]
