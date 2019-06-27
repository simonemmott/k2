from django.db import models
from django.template.defaultfilters import pluralize
from .domain import Domain
from .member import Member
from .field import Field

import k2_util

class Model(models.Model):
    name = models.CharField('Name', max_length=50, blank=False, null=False)
    title = models.CharField('Title', max_length=90, blank=False, null=False)
    p_title = models.CharField('Plural title', max_length=90, blank=True, null=True)
    description = models.TextField('Description', blank=True, null=True)
    admin_model = models.BooleanField('Admin Model', blank=True, null=True, default=False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='models')
    # members list of Members of Model
    # members_with_data_type list of Members with this model as a data type
    
    def fields(self):
        return self.members.filter(type=Member.Type.FIELD)
    
    def type_fields(self):
        types = []
        for member in self.fields():
            if member.field.field_type == Field.FieldType.SUB_TYPE:
                types.append(member.field)
        return types
    
    def __str__(self):
        return self.title
    
    def class_name(self):
        return k2_util.to_class_case(self.name)
    
    def package_name(self):
        return k2_util.to_snake_case(self.name)
    
    def fields(self):
        return Field.objects.filter(model=self)
    
    def plural_title(self):
        return self.p_title if self.p_title else k2_util.to_plural(self.title)