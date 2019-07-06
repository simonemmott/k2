from django.db import models
from .member import Member
from k2_core.mixins.module import ModuleMixin
from .base_type import BaseType

class Module(BaseType, ModuleMixin):
    
    package = models.ForeignKey('Package', on_delete=models.CASCADE, related_name='modules', blank=False, null=True)
    