from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from core.models import Log
from core.serializers import LogSerializer, CustomAuthTokenSerializer


class CustomObtainAuthToken(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = CustomAuthTokenSerializer


class UseCreatedToken(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({'request': request.headers})


class LogeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = LogSerializer
    queryset = Log.objects.all()

# Create your views here.
