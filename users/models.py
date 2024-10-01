from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    is_host = models.BooleanField(default=False)  # Whether the user is a host
    bio = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)  # Optional field for contact

    def __str__(self):
        return self.user.username
