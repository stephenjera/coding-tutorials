from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import WebsiteUser

admin.site.register(WebsiteUser, UserAdmin)
