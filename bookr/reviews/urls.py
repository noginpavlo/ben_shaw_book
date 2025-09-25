from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="welcome_view"),
    path("books/", views.book_list, name="book_list"),
]
