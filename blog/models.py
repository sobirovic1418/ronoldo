from django.db import models

class Book(models.Model):
    title=models.CharField(max_length=205)
    author=models.CharField(max_length=202)
    description=models.TextField()

    def __str__(self):
        return self.title