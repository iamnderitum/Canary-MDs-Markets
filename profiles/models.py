from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    image = models.ImageField(
        upload_to="profiles",
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        blank=True
    )
    bio = models.TextField(
        blank=True,
        null=True
    )
    profession = models.CharField(
        max_length=30,
        blank=True,
        null=True
    )

    dob = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    address = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        null=True,
        blank=True
    )

    def __str__(self):
        #  return f"Profile for {self.user.username}" # self.user.username
        return self.user.get_username()