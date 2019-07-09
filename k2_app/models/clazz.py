from django.db import models
from .member import Member
from k2_core.mixins.clazz import ClazzMixin
from .base_type import BaseType

class Clazz(BaseType, ClazzMixin):
    
    foo = models.CharField('Foo', max_length=50, blank=False, null=True)
    