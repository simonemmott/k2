from rest_framework import serializers
from k2_app.models.package import Package
from rest_framework_recursive.fields import RecursiveField

class PackageSerializer(serializers.ModelSerializer):
    modules = RecursiveField('k2_app.serializers.module.ModuleSerializer', many=True, required=False)
    class Meta:
        model = Package
        fields = ['name', 'version', 'description', 'modules']