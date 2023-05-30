from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions

from apps.feedback.serializers import FeedbackSerializer, FavoriteSerializer
from apps.feedback.managers import FeedbackMessageManager
from apps.feedback.models import Favorite
from apps.posts.models import Post
from apps.posts.permissions import IsOwnerOrReadOnly


class FeedbackMessageCreateView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        feedback_message = serializer.save(user=self.request.user)
        return FeedbackMessageManager.perform_create(
            feedback_message, self.request.user
        )


class FavoriteCreateDestroyView(
    generics.CreateAPIView, generics.DestroyAPIView
):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        serializer.save(user=self.request.user, post=post)


class FavoriteListView(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self):
        user = self.request.user
        return get_object_or_404(Favorite, user=user)
