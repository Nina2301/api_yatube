from posts import models
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    group = serializers.SlugRelatedField(
        queryset=models.Group.objects.all(),
        slug_field='slug',
        required=False)

    class Meta:
        model = models.Post
        fields = ('id', 'text', 'author', 'image', 'pub_date', 'group')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = models.Comment
        fields = ('id', 'text', 'author', 'post', 'created')
