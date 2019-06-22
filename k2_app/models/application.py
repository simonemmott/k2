from django.db import models
from rest_framework import serializers
import random
from k2_app.models import application_domain

class Application(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=90)
    description = models.TextField()
    # application_domains list ApplicationDomains for application
    
    def __str__(self):
        return self.title
    
    def secret(self):
        return ''.join(random.choice('abcdefghighjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(90))

class ApplicationSerializer(serializers.ModelSerializer):
    application_domains = application_domain.ApplicationDomainSerializer(many=True)
    class Meta:
        model = Application
        fields = ('id', 'name', 'title', 'description', 'application_domains')   