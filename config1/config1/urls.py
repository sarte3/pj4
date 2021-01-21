from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls), #127.0.0.1:8000/admin
    path('polls/', include('polls.urls')), #127.0.0.1:8000/polls
    path('member/', include('member.urls')), #127.0.0.1:8000/member
    # path('polls/', include('member.urls)), #127.0.0.1:8000/member
]
