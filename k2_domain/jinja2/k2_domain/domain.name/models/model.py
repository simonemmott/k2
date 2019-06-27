from django.db import models

class {{model.class_name()}}(models.Model):
{% for field in model.fields() %}    {{field.name}} = models.{{field.field_class_name()}}('{{field.title_or_link_type()}}'{{field.model_field_options()}})
{% endfor %}
