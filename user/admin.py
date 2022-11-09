from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from home.forms import RegistrationForm
from .models import CustomUser
user=get_user_model()
# Register your models here.

class UserAdmins(UserAdmin):
    add_form = RegistrationForm
    # add_form = UserFormChange
    readonly_fields = ['reciept']
    list_display = [
        'email',
        'name',
        'is_admin',
        'reciept',
    ]

    list_filter =[
        'is_admin'
    ]
    fieldsets = [
        (None, {
            'fields': ['email', 'password']
        }),
        ('Personal Field', {
            'fields': ['name', 'reciept']
        }),
        ('Permissions', {
            'fields': ['is_admin', 'is_confirm']
        })
    ]
    add_fieldsets = [
        (None, {
            'classes': ['wide'],
            'fields': ['email', 'name', 'password1', 'password2']
        })
    ]
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = []
admin.site.register(CustomUser, UserAdmins)
# admin.site.register(user)