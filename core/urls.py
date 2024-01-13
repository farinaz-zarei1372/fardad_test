from django.urls import path

from .views import CustomAuthToken, UseCreatedToken

urlpatterns = [
    path('get_token/', CustomAuthToken.as_view()),
    path('use_token/', UseCreatedToken.as_view()),
]
