from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from core.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ["id", "content", "created_at", "updated_at"]


class CustomAuthTokenSerializer(AuthTokenSerializer):
    def create(self, validated_data):
        token, created = Token.objects.get_or_create(user=validated_data["user"])
        return {'token': token.key}
