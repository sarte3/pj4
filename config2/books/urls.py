from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'books'

urlpatterns = [
    path('book/', views.BookList.as_view(), name='booklist'),
    path('publisher/', views.PublisherList.as_view(), name='publisherlist'),
    path('publisher/<int:pk>/', views.PublisherDetail.as_view(), name='publisherdetail'),
    path('', views.BooksIndexView.as_view(), name='index'),
    path('publisher/insert', views.PublisherCreate.as_view(), name='publisherinsert')
]
# as_view() 메소드 -  진입메소드,
# urls.py에서 클래스형 뷰의 as_view() 메소드를 호출