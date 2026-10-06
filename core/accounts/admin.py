from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User, Profile
# Register your models here.

# I learning UserCreationForm but I won't use it in the project 
# from django.contrib.auth.forms import UserCreationForm
# class CustomUserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = UserCreationForm + ('email',)
# we write this code at the CustomUserAdmin   
# add_form = CustomUserCreationForm


class CustomUserAdmin(UserAdmin):
    model = User
    
    list_display = ('email','is_superuser','is_active', 'is_verified')
    list_filter = ('email','is_superuser','is_active', 'is_verified')
    search_fields = ('email',)
    ordering = ('email',)

    fieldsets = (
        ('Authentication', {
            "fields": (
                'email', 'password'
            ),
        }),

        ('Permissions', {
            "fields": (
                'is_active', 'is_staff','is_superuser', 'is_verified'
            ),
        }),

        ('user_permissions', {
            "fields": (
                'groups', 'user_permissions'
            ),
        }),

         ('important date', {
            "fields": (
                'last_login',
            ),
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            "fields": (
                'email', 'password1', 'password2', 'is_active', 'is_staff','is_superuser', 'is_verified'
            ),
        }),
    )
    

admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)