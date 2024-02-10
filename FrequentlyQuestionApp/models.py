from django.db import models


# Create your models here.
class FrequentlyQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    page = models.CharField(max_length=50)

    def __str__(self):
        return self.question
