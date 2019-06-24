from django.db import models

class {{model.class_name()}}(models.Model):
{% for field in model.fields() %}    {{field.name}} = models.{{field.field_class_name()}}('{{field.title}}'{{field.default_clause()}}{{field.max_length_clause()}}{{field.blank_clause()}}{{field.null_clause()}})
{% endfor %}
