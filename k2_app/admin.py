from django.contrib import admin
from .models import Application
from .models import ApplicationDomain
from .models import BaseType
from .models import Package
from .models import Module
from .models import Member

admin.site.register(Application)
admin.site.register(ApplicationDomain)
admin.site.register(BaseType)
admin.site.register(Package)
admin.site.register(Module)
admin.site.register(Member)
