from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("event/user", views.user_birthday, name="user"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
