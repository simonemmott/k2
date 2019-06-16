from django.contrib import admin
from .models import Domain
from .models import Model

# Register your models here.
admin.site.register(Domain)
admin.site.register(Model)
