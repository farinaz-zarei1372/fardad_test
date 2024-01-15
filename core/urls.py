from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UseCreatedToken, LogeViewSet, CustomObtainAuthToken

router = DefaultRouter()
router.register(r'log', LogeViewSet, basename="log")
router.register(r'get_token', CustomObtainAuthToken, basename="log")

urlpatterns = [
    path('use_token/', UseCreatedToken.as_view()),
]
urlpatterns += router.urls
