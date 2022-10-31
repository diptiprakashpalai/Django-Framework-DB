from django.urls import path
from . import views
 
urlpatterns = [path("", views.index),
               path("index", views.indexdb),
               path("book_detail", views.book_detail),
               path("task", views.task),
               path("taskDetails", views.taskDetails)]