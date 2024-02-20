from django.contrib import admin
from .models import *


class ContactAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email', 'phone',
                    'address')
    search_fields = ['user']


admin.site.register(Contact, ContactAdmin)


class SiteAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'url', 'username',
                    'password')
    search_fields = ['user']


admin.site.register(Site, SiteAdmin)