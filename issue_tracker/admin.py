from django.contrib import admin

from issue_tracker.models import Registry


class RegistryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Registry, RegistryAdmin)
