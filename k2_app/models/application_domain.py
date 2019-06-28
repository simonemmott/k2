from django.db import models
from rest_framework import serializers
from k2_domain.models import Domain
from k2_core.mixins.application_domain import ApplicationDomainMixin

class ApplicationDomain(models.Model, ApplicationDomainMixin):
    application = models.ForeignKey('Application', on_delete=models.CASCADE, related_name='application_domains')
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    
    
class ApplicationDomainSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='domain.id')
    name = serializers.CharField(source='domain.name')
    class Meta:
        model = ApplicationDomain
        fields = ('id', 'name')
        