from django.contrib import admin
from .models import Application
from .models import ApplicationDomain

admin.site.register(Application)
admin.site.register(ApplicationDomain)
