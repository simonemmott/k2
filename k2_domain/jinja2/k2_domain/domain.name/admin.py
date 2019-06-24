from django.contrib import admin
{% for model in domain.models.filter(admin_model=True) %}from .models import {{model.class_name()}}
{% endfor %}

# Register your models here.
{% for model in domain.models.filter(admin_model=True) %}admin.site.register({{model.class_name()}})
{% endfor %}
