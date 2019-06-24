from django.db import models
from .domain import Domain
import k2_util

class Model(models.Model):
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    title = models.CharField('Title', max_length=90, blank=False, null=False)
    description = models.TextField('Description', blank=True, null=True)
    admin_model = models.BooleanField('Admin Model', blank=True, null=True, default=False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='models')
    # members list of Members of Model
    # members_with_data_type list of Members with this model as a data type
    
    def __str__(self):
        return self.title
    
    def class_name(self):
        return k2_util.to_class_case(self.name)
    
    def package_name(self):
        return k2_util.to_snake_case(self.name)