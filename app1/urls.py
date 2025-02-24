from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename="author_api")
router.register(r'books', BookViewSet, basename="book_api")

urlpatterns = [
    path('', include(router.urls)),
]
