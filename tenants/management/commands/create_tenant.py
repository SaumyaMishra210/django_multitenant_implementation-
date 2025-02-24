from tenants.models import Tenant, Domain

# Ensure public tenant exists
public_tenant, created = Tenant.objects.get_or_create(schema_name="public", defaults={"name": "Public Tenant"})

# Map public schema to localhost
Domain.objects.get_or_create(domain="127.0.0.1", tenant=public_tenant, defaults={"is_primary": True})
Domain.objects.get_or_create(domain="example.com", tenant=public_tenant, defaults={"is_primary": False})
