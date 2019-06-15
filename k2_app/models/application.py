from django.db import models
import random

class Application(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=90)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    
    def secret(self):
        return ''.join(random.choice('abcdefghighjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(90))

    