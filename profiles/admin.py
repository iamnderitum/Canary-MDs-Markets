from django.contrib import admin
from django.utils.html import format_html
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    #model = Profile
    list_display = [
        "user",
        "profile_image",
        "phone",
        "profession",
        "dob",
        "city",
    ]
    list_filter = [
        "profession",
        "created",
    ]
    def profile_image(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" height="60" '
                'style=obect-fit:cover; border-radius:50% />',
                obj.image.url,
            )

        return "No Image"

    profile_image.short_description = "Profile Image"

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                'img src="{}" width="150" height="150" '
                'style="object-fit: cover; border-radius: 50;" />',
                obj.image.url,
            )
        return "No Image uploaded"

    image_preview.short_description = "Current Profile Image"