from django.db import models
from ..models import Application

class ApplicationDomain(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='application_domains')
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    title = models.CharField('Title', max_length=90, blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    
    def __str__(self):
        return self.title