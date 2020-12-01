from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    picture = models.ImageField()
    description = models.TextField()
    link = models.URLField(blank=True)