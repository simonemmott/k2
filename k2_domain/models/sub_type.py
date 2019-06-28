from django.db import models
from .field import Field
from k2_core.mixins.sub_type import SubTypeMixin

class SubType(models.Model, SubTypeMixin):
    name = models.CharField('Name', max_length=30, blank=False, null=False)
    value = models.CharField('Value', max_length=3, blank=False, null=False)
    label = models.CharField('Label', max_length=50, blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='sub_types')
        