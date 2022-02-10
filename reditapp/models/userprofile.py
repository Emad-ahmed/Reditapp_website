from django.db import models
from reditapp.models import Registration


class UserProfile(models.Model):
    user = models.OneToOneField(
        Registration, on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to='images/', blank=True)
