from django.db import models
from .domain import Domain
from .member import Member
from .field import Field
from k2_core.mixins.model import ModelMixin
from .base_type import BaseType

import k2_util

class Model(BaseType, ModelMixin):
    title = models.CharField('Title', max_length=90, blank=False, null=False)
    p_title = models.CharField('Plural title', max_length=90, blank=True, null=True)
    admin_model = models.BooleanField('Admin Model', blank=True, null=True, default=False)
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='models')
    # members list of Members of Model
    # members_with_data_type list of Members with this model as a data type
    