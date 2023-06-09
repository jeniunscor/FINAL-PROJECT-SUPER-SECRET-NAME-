from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User, Region, City


@admin.register(User)
class UserAdmin(UserAdmin):
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': (
            'number',
            'avatar',
            'gender',
            'is_admin',
            'city',
            'region',

        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )
    list_display = (
        'email',
        'gender',
        'is_active',
        'is_staff',

    )


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass
