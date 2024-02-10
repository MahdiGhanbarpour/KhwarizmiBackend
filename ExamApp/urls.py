from django.urls import path

from . import views

urlpatterns = [
    path("exams", views.getExams),
    path("popular-exams", views.getPopularExams),
    path("exam-questions", views.getExamsQuestion),
]
