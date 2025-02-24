from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from django_tenants.utils import schema_context
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class TenantAwareViewSet(viewsets.ModelViewSet):
    """ Base view to automatically use the current tenant schema """

    def get_queryset(self):
        schema_name = self.request.tenant.schema_name  # Detect current tenant schema
        with schema_context(schema_name):
            return self.queryset.all()

    def perform_create(self, serializer):
        schema_name = self.request.tenant.schema_name
        with schema_context(schema_name):
            serializer.save()


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
