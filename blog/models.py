from django.db import models

class Blog(models.Model):

    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title