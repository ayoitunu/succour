from django.conf.urls import url, include
from django.contrib.auth.models import User
from . import models
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class DesignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Designer
        fields = ['url', 'first_name', 'last_name', 'phone_number', 'facebook_link', 'instagram_link', 'linkedin_link']


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Category
        fields = ['url', 'category_name']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['url', 'text', 'image', 'user_id', 'comments', 'category_id']
        read_only_fields = ['date_posted']
