from webui.models import MemberList
from rest_framework import serializers

class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberList
        fields = '__all__'