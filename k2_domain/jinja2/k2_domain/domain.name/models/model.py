from django.db import models

class {{model.class_name()}}(models.Model):
    
{% for type_field in model.type_fields() %}
    class {{type_field.types_name()}}:
        {% for sub_type in type_field.sub_types.all() %}
        {{sub_type.type_name()}} = '{{sub_type.type_value()}}'
        {% endfor %}
        CHOICES = [
            {% for sub_type in type_field.sub_types.all() %}
            ({{sub_type.type_name()}}, '{{sub_type.label}}'),
            {% endfor %}
        ]
        
{% endfor %}
{% for field in model.fields() %}
    {{field.name}} = models.{{field.field_class_name()}}('{{field.title_or_link_type()}}'{{field.model_field_options()}})
{% endfor %}
