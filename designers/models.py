from django.db import models
from django.contrib.auth.models import User


class Designer(models.Model):
    phone_number = models.CharField(max_length=25)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    facebook_link = models.URLField(blank=True)
    instagram_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)


