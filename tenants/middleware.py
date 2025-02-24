# tenants/middleware.py
from django_tenants.middleware import TenantMiddleware


class CustomTenantMiddleware(TenantMiddleware):
    pass  # You can extend this class if you need custom logic
