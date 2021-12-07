from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=100)
    top_speed = models.IntegerField()

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
      
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)
      
    def __str__(self):
        return self.title        