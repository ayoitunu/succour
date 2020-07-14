from django.contrib.auth.models import User
from . import models
from rest_framework import serializers


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class DesignerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Designer
        fields = ['user', 'phone_number', 'facebook_link', 'instagram_link', 'linkedin_link']



