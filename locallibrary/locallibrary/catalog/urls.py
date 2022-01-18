from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-author', views.AuthorCreateView.as_view(), name="add-author"),
]