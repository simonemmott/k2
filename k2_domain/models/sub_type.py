from django.db import models
from .field import Field

class SubType(models.Model):
    name = models.CharField('Name', max_length=30, blank=False, null=False)
    value = models.CharField('Value', max_length=3, blank=False, null=False)
    label = models.CharField('Label', max_length=50, blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    field = models.ForeignKey(Field, on_delete=models.CASCADE, related_name='sub_types')
    
    def __str__(self):
        return self.label
    
    def type_name(self):
        return self.name.upper()

    def type_value(self):
        return self.value.upper()
    