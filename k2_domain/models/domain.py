from django.db import models
from k2_core.mixins.domain import DomainMixin


class Domain(models.Model, DomainMixin):
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    title = models.CharField('Title', max_length=90, blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    # models list Model for domain
    