from django.db import models
from rest_framework import serializers
from k2_app.models import application_domain
from k2_core.mixins.application import ApplicationMixin


class Application(models.Model, ApplicationMixin):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=90)
    description = models.TextField()
    # application_domains list ApplicationDomains for application
        

class ApplicationSerializer(serializers.ModelSerializer):
    application_domains = application_domain.ApplicationDomainSerializer(many=True)
    class Meta:
        model = Application
        fields = ('id', 'name', 'title', 'description', 'application_domains')   