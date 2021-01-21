from django.urls import path
from django.urls import include
from . import views

app_name='polls'
urlpatterns = [
    # path(url패턴, url이 매칭되면 호출되는 뷰함수와 인자[, 이름]),
    path('', views.index, name='list'), #127.0.0.1:8000/polls
    path('<int:qid>/', views.detail, name='detail'), #127.0.0.1:8000/polls/2
    path('vote/<int:qid>/', views.vote, name='vote1'),
    path('dbtest/', views.dbtest),
    # path('insert/', views.insert), #127.0.0.1:8000/polls/insert
]
