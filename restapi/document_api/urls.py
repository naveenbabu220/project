from django.contrib import admin
from django.urls import path , include
from rest_framework.routers import DefaultRouter
from document_api.views import DocumentViewset


router = DefaultRouter()
router.register(r'documents', DocumentViewset)
urlpatterns = [
    path('',include(router.urls))
]