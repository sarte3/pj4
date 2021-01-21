from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert), #127.0.0.1:8000/member/insert   
]
