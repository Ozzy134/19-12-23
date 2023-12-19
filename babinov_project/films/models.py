from django.db import models

class Films(models.Model):
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=15)
    date = models.DateField()
    artist = models.TextField()


