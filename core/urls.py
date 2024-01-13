from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CustomAuthToken, UseCreatedToken, LogeViewSet

router = DefaultRouter()
router.register(r'log', LogeViewSet, basename="log")

urlpatterns = [
    path('get_token/', CustomAuthToken.as_view()),
    path('use_token/', UseCreatedToken.as_view()),
]
urlpatterns += router.urls
