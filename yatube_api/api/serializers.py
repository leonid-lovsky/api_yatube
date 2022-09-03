from rest_framework import serializers

from posts.models import Comment, Post, Group


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'created')


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
