from django.db import models


# Create your models here
class Exam(models.Model):
    name = models.CharField(max_length=30)
    image = models.TextField()
    description = models.TextField()
    authorName = models.CharField(max_length=30)
    authorPhoneNum = models.CharField(max_length=11, default=None, blank=True, null=True)
    rating = models.FloatField()
    difficulty = models.CharField(max_length=15)
    grade = models.CharField(max_length=7)
    price = models.IntegerField()
    isVerified = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.TextField()
    grade = models.CharField(max_length=7)
    parentExamId = models.IntegerField()

    def __str__(self):
        return self.question


class Option(models.Model):
    option = models.CharField(max_length=100)
    isCorrect = models.BooleanField()
    parentQuestionId = models.IntegerField()

    def __str__(self):
        return self.option


class Attachment(models.Model):
    detail = models.TextField(default=None, blank=True, null=True)
    image = models.TextField()
    parentQuestionId = models.IntegerField()

    def __str__(self):
        return self.image
