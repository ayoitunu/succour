from django.contrib.auth.models import User
from rest_framework import routers, viewsets
from . import serializers, models


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class DesignerViewSet(viewsets.ModelViewSet):
    queryset = models.Designer.objects.all()
    serializer_class = serializers.DesignerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer


