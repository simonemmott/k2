from rest_framework import serializers
from k2_app.models.clazz import Clazz
from rest_framework_recursive.fields import RecursiveField

class ClazzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clazz
        fields = ['id', 'name', 'description', 'type', 'foo']
        read_only_fields = ['id']
        
    def create(self, validated_data):
        return Clazz.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.type = validated_data.get('type', instance.type)
        instance.foo = validated_data.get('foo', instance.foo)
        return instance