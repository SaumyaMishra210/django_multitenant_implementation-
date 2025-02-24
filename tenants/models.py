# tenants/models.py
from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from datetime import date


class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    subdomain = models.CharField(max_length=255)
    created_on = models.DateField(default=date.today)

    # Default schema on tenant creation
    auto_create_schema = True
    auto_drop_schema = True  # Caution: Drops schema when tenant is deleted!

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    pass
