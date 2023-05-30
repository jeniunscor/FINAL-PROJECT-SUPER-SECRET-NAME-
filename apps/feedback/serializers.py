from rest_framework import serializers

from apps.feedback.models import Feedback, Favorite

from apps.posts.serializers import PostSerializer
from apps.users.serializers import UserSerializer


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = (
            'user',
            'name',
            'contact',
            'message',
        )


class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    post = PostSerializer(read_only=True)

    class Meta:
        model = Favorite
        fields = [
            'id', 'user', 'post'
        ]
