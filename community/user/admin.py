from django.contrib import admin
from .models import User


class CommunityAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(User, CommunityAdmin)
