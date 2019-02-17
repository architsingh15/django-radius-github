from django.contrib import admin
from django.contrib.auth.models import User, Group

from issue_tracker.models import Registry


class RegistryAdmin(admin.ModelAdmin):
    pass


# adds registry model in admin page
admin.site.register(Registry, RegistryAdmin)

# removes group and user model in admin page
admin.site.unregister(Group)
admin.site.unregister(User)

# renames different headers in admin page
admin.site.site_header = "Issue Tracker Admin"
admin.site.site_title = "Issues"
admin.site.index_title = "Welcome to Issue Tracker Admin"
