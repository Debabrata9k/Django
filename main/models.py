from django.db import models

class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="🔥") 

    def __str__(self):
        return self.title
