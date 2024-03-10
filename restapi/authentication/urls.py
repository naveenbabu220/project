from django.urls import path
from .authentication import SimpleAuthentication

urlpatterns = [
    path('auth/', SimpleAuthentication),
]