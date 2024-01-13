from rest_framework import serializers

from core.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ["id", "content", "created_at", "updated_at"]
