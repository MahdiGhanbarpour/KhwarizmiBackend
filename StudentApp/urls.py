from django.urls import path

from . import views

urlpatterns = [
    path("login", views.loginStudent),
    path("register", views.registerStudent),
]
