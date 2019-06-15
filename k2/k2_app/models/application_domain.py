from django.db import models
from ..models import Application
from k2_domain.models import Domain

class ApplicationDomain(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='application_domains')
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.domain.title