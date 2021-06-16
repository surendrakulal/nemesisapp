from django.contrib import admin
from users.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'email', 'password', 'confirm_password', 'address')
    search_fields =('email', 'username')
    readonly_fields=('date_joined', 'last_login')
    ordering = ('id',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(User, UserAdmin)