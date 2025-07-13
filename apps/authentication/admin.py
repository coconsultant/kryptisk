from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

# Create a mutable copy of the default UserAdmin fieldsets
modified_fieldsets = list(UserAdmin.fieldsets)

# Define the custom fields to add to the "Personal info" section
custom_personal_fields = ("avatar", "social_twitter", "social_facebook", "social_instagram", "bio")

# Find the "Personal info" fieldset and extend its fields
for i, (name, options) in enumerate(modified_fieldsets):
    if name == _('Personal info'):
        existing_fields = list(options['fields'])
        # Add new fields if they are not already present
        for field in custom_personal_fields:
            if field not in existing_fields:
                existing_fields.append(field)
        modified_fieldsets[i] = (name, {'fields': tuple(existing_fields)})
        break # Stop after modifying the correct fieldset

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Assign the modified fieldsets to the class attribute
    fieldsets = tuple(modified_fieldsets)

    # add_fieldsets is for the user creation form.
    # Assuming "Personal info" fields (first_name, last_name, email) are not
    # by default in UserAdmin.add_fieldsets, this addition typically won't cause duplicates.
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name", "email",)}),
    )

    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "first_name", "last_name", "email")
    ordering = ("username",)
