from rest_framework import serializers
from k2_app.models.base_type import BaseType
from rest_framework_recursive.fields import RecursiveField


class DataTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseType
        fields = ['name']
        extra_kwargs = {
            'name': {
                'validators': []
            }
        }
