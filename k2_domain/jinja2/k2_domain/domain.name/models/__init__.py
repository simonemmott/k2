{% for model in domain.models.all() %}from .{{model.package_name()}} import {{model.class_name()}}
{% endfor %}