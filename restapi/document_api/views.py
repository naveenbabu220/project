from django.shortcuts import render
from rest_framework import viewsets
from .models import Document
from .serializers import DocumentSerializer

# Create your views here.

class DocumentViewset(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer