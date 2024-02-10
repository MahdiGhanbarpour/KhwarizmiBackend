from django.contrib import admin

from ExamApp.models import Exam, Question, Option, Attachment

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Attachment)
