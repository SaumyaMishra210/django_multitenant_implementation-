from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="tenant-home"),
    # path('create/', create_tenant, name='create_tenant'),  # Create a new tenant
    # path('list/', list_tenants, name='list_tenants'),  # List all tenants
]
