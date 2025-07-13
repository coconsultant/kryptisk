from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Customize the forms and how fields are displayed in the admin
    fieldsets = UserAdmin.fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email", "avatar", "social_twitter", "social_facebook", "social_instagram", "bio")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email",)}),
    )

    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
