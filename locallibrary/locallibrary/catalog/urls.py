from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-author', views.AuthorCreateView.as_view(), name="add-author"),
    path('add-book', views.new_book, name="add-book"),
    path('book/<int:pk>/renew', views.renew_book_librarian, name='renew-book-librarian'),
]

# book/12/renew
# catalog/book/2