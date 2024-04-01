from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from first.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name',)
    search_fields = ('email', 'first_name', 'last_name', 'username',)
    readonly_fields = ('last_login', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'is_superuser',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (
            'Personal Info',
            {'fields': ('first_name', 'last_name', 'email')}
        ),
        (
            'Permission',
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (
            'Impotent dates',
            {'fields': ('last_login', 'date_joined')}
        )
    )

# Register your models here.
