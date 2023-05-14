from django.urls import path
from book.views import BooksView, BooksDetailView 


app_name = 'books'

urlpatterns = [
    path('', BooksView.as_view(), name='list'),
    path("<int:id>/", BooksDetailView.as_view(), name='detail'),
]