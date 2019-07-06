from django.db import models
from .domain import Domain
from .member import Member
from .field import Field
from k2_core.mixins.base_type import BaseTypeMixin

import k2_util

class BaseType(models.Model, BaseTypeMixin):
    class Type:
        MODULE = 'MOD'
        CLASS = 'CLS'
        MODEL = 'MDL'
        VIEW = 'VEW'
        SERIALIZER = 'SZR'
        CHOICES = [
            (MODULE, 'Module'),
            (CLASS, 'Class'),
            (MODEL, 'Model'),
            (VIEW, 'View'),
            (SERIALIZER, 'Serializer'),
        ]

    name = models.CharField('Name', max_length=1024, blank=False, null=False, unique=True)
    description = models.TextField('Description', blank=True, null=True)
    type = models.CharField('Type', max_length=3, choices=Type.CHOICES, default=Type.MODULE, blank=False, null=False)
    # members list of Members of Model
    # members_with_data_type list of Members with this model as a data type
    
    
        