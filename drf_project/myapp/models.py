from django.db import models


# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=30)
    age=models.TextField()
    email=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name