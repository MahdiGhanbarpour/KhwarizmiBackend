from django.db import models


# Create your models here.
class Student(models.Model):
    phoneNumber = models.CharField(max_length=11, primary_key=True)

    fullName = models.CharField(max_length=30)
    birthday = models.CharField(max_length=15)
    grade = models.CharField(max_length=7)

    def __str__(self):
        return self.fullName
