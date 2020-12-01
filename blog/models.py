from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    date = models.DateField()
    content = models.TextField()

    def __str__(self):# to call the object in the database the field title
        return self.title