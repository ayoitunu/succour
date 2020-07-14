from django.contrib.auth.models import User
from rest_framework import viewsets
from . import serializers, models


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class DesignerViewSet(viewsets.ModelViewSet):
    queryset = models.Designer.objects.all()
    serializer_class = serializers.DesignerSerializer




