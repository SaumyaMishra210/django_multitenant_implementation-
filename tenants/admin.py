from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Tenant)
# admin.site.register(TenantAwareModel)
admin.site.register(Domain)
