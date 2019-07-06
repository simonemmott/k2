from django.db import models
from .member import Member
from k2_core.mixins.package import PackageMixin

import k2_util

class Package(models.Model, PackageMixin):

    name = models.CharField('Name', max_length=1024, blank=False, null=True, unique=True)
    version = models.CharField('Version', max_length=20, blank=False, null=True)
    description = models.TextField('Description', blank=True, null=True)
    # modules list of Modules in package
    
    
        