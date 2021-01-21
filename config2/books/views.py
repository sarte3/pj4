from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Book, Publisher, Author
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView

class BookList(ListView):
    model = Book

class PublisherList(ListView):
    model = Publisher

class PublisherDetail(DetailView):
    model = Publisher

class PublisherCreate(CreateView):
    model = Publisher
    fields = ['name', 'addr', 'website'] # 입력 받을 컬럼 지정
    template_name = 'books/publisherinsert.html'
    success_url = '/books' # CreateView, UpdateView, DeleteView를 사용시 특정 기능 수행 후 어떤 페이지로 이동할지 지정

class BooksIndexView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mlist']=['book', 'publisher', 'author']
        return context
