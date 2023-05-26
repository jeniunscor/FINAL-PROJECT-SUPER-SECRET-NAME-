from rest_framework import serializers
from apps.posts.models import Category, Post, Commentary


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "name",
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "subtitle",
            "category",
            "description",
            "post_image",
            'is_active',
        )


class CommentarySerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Commentary
        fields = [
            'id',
            'description',
            'author',
            'post',
        ]
