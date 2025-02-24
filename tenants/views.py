from django.shortcuts import render
from django.http import HttpResponse
from django_tenants.utils import get_tenant_model

def home(request):
    tenant = request.tenant  # Get the current tenant

    # DEBUG: Print tenant info
    print(f"Schema: {tenant.schema_name}")
    print(f"Tenant Name: {getattr(tenant, 'name', 'No Name Found')}")

    if not hasattr(tenant, "name") or not tenant.name:
        return HttpResponse("Tenant name is missing. Check your database.")

    context = {
        "tenant_name": tenant.name,  # Get name safely
        "schema_name": tenant.schema_name,
    }

    return render(request, "public_page.html", context)
