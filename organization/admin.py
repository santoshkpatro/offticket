from django.contrib import admin

from organization.models import Organization


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('org_username', 'org_name', 'is_org_verified')