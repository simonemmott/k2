from rest_framework import serializers
from k2_app.models.module import Module
from rest_framework_recursive.fields import RecursiveField
from k2_app.serializers.member import MemberSerializer
from k2_core.serializers import RelatedModelSerializer
from k2_util import strip_dict


class ModuleSerializer(RelatedModelSerializer):
    
    members = MemberSerializer(many=True, required=False)
    
    class Meta:
        model = Module
        fields = ['name', 'type', 'description', 'members']
        read_only_fields = ['members']
        extra_kwargs = {
            'name': {
                'validators': []
            }
        }
        instance_fields = ['name', 'type', 'description']
        related_fields = [
                ('members', MemberSerializer, 'members')
            ]
        
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.description = validated_data.get('description', instance.description)
        return instance
