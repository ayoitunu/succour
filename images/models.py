from django.db import models
from django.contrib.auth.models import User


class Designer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=25)
    facebook_link = models.URLField()
    instagram_link = models.URLField()
    linkedin_link = models.URLField()


class Category(models.Model):
    category_name = models.CharField(max_length=255)


class Post(models.Model):
    text = models.CharField(max_length=2500)
    images = models.ImageField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField()
    comments = models.CharField(max_length=2500)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)






