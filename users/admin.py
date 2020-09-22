from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.

from users.models import User, Profile


class CustomUserAdmin(UserAdmin):
    """User model admin."""

    list_display = ('email', 'username', 'first_name',
                    'last_name', 'is_staff', 'is_client')

    list_filter = ('is_client', 'is_staff', 'created_at', 'updated_at')

class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin."""

    list_display = ('user')


admin.site.register(User, CustomUserAdmin)