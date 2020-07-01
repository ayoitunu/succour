
from django.contrib.auth.models import User
from rest_framework import routers, viewsets
from . import serializers

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

