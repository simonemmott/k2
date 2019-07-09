from rest_framework import serializers
from k2_app.models.package import Package
from rest_framework_recursive.fields import RecursiveField
from k2_app.serializers.module import ModuleSerializer
from k2_core.serializers import RelatedModelSerializer
from k2_util import strip_dict

import logging
logger = logging.getLogger(__name__)

class PackageSerializer(RelatedModelSerializer):
    
    modules = ModuleSerializer(many=True, required=False)
    
    class Meta:
        model = Package
        fields = ['id', 'name', 'version', 'description', 'modules']
        read_only_fields = ['id']
        instance_fields = ['name', 'version', 'description']
        related_fields = [
                ('modules', ModuleSerializer, 'modules')
            ]
        
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.version = validated_data.get('version', instance.version)
        instance.description = validated_data.get('description', instance.description)
        return instance
    