from . import models
from rest_framework import serializers


class PostCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostCategory
        fields = ['category_name']
        read_only_fields = ['date_posted']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Post
        fields = ['text', 'voice', 'designer', 'category']
        read_only_fields = ['date_posted']


class PostImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostImage
        fields = ['post_image', 'post']


class PostLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostLike
        fields = ['user', 'post']
        read_only_fields = ['date_posted']


class PostCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostComment
        fields = ['user', 'comment_text', 'post']
        read_only_fields = ['date_posted']


class PostCreditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostCredit
        fields = ['user', 'post']
        read_only_fields = ['date_posted']


class PostShareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostShare
        fields = ['user', 'post', 'platform']
        read_only_fields = ['date_posted']


class PostCommentCommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostCommentComment
        fields = ['user', 'post_comment', 'text']
        read_only_fields = ['date_posted']


class PostCommentLikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PostCommentLike
        fields = ['user', 'post_comment']
        read_only_fields = ['date_posted']
