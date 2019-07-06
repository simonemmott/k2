from django.contrib import admin
from .models import Domain
from .models import Model
from .models import Field
from .models import SubType

# Register your models here.
admin.site.register(Domain)
admin.site.register(Model)
admin.site.register(Field)
admin.site.register(SubType)
