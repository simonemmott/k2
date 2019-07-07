from rest_framework import serializers
from k2_app.models.module import Module
from rest_framework_recursive.fields import RecursiveField


class ModuleSerializer(serializers.ModelSerializer):
    members = RecursiveField('k2_app.serializers.member.MemberSerializer', many=True, required=False)
    class Meta:
        model = Module
        fields = ['name', 'type', 'description', 'members']