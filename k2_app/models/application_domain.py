from django.db import models
from rest_framework import serializers
#from k2_app.models.application import Application
from k2_domain.models import Domain

class ApplicationDomain(models.Model):
    application = models.ForeignKey('Application', on_delete=models.CASCADE, related_name='application_domains')
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.domain.title
    
class ApplicationDomainSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='domain.id')
    name = serializers.CharField(source='domain.name')
    class Meta:
        model = ApplicationDomain
        fields = ('id', 'name')
        