from rest_framework import serializers
from k2_app.models.member import Member
from k2_app.models.base_type import BaseType
from rest_framework_recursive.fields import RecursiveField
from k2_app.serializers.base_type import DataTypeSerializer
from k2_core.serializers import RelatedModelSerializer
from k2_util import strip_dict
import logging

logger = logging.getLogger(__name__)


class MemberSerializer(RelatedModelSerializer):
    
    data_type = DataTypeSerializer(required=False, allow_null=True)

    class Meta:
        model = Member
        fields = ['name', 'member_type', 'title', 'description', 'data_type']
        read_only_fields = ['data_type']
        instance_fields = ['name', 'member_type', 'title', 'description']
        

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.member_type = validated_data.get('member_type', instance.member_type)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        if 'data_type' in validated_data:
            instance.data_type = BaseType.objects.get(name=validate_data.get('data_type')['name'])
        return instance
    
