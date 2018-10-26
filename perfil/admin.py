from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from perfil.models import Perfil

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    """ Extender modelo de usuario de python"""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = ('user__email', 'user__username', 'user__first_name', 'user__last_name', 'phone_number')

    list_filter = ('created', 'modified', 'user__is_active', 'user__is_staff')

    fieldsets = (
        ('Profile', {
            'fields': (
                ('user', 'picture'),
            )
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (
                ('created', 'modified')
            )
        })
    )

    readonly_fields = ('created', 'modified')

class PerfilsInline(admin.StackedInline):
    """ In-line profile for users in administrator """

    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfils'

class UserAdmin(BaseUserAdmin):
    """ Add profile admin to base user admin. """

    inlines = (PerfilsInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)