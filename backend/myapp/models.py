from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    cuisine = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    rating = models.FloatField()
    type = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name