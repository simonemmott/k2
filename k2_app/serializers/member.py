from rest_framework import serializers
from k2_app.models.member import Member
from rest_framework_recursive.fields import RecursiveField


class MemberSerializer(serializers.ModelSerializer):
    data_type = RecursiveField('k2_app.serializers.base_type.DataTypeSerializer', required=False)
    class Meta:
        model = Member
        fields = ['name', 'member_type', 'title', 'description', 'data_type']