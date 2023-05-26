from django.shortcuts import render, get_object_or_404
from requests import Response

from rest_framework import generics, permissions, status
from .models import Commentary, Post
from .serializers import PostSerializer, CommentarySerializer
from .permissions import (
    IsOwnerOrReadOnly,
    IsBuyerOrReadOnly,
    IsSellerOrReadOnly,
)


class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsSellerOrReadOnly]

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.AllowAny,)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        if 'is_active' in request.data:
            if instance.author != request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            instance.is_active = request.data['is_active']
            instance.save()
            return Response(status=status.HTTP_200_OK)
        return super().partial_update(request, *args, **kwargs)


class CommentCreateView(generics.CreateAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyerOrReadOnly]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs['post_pk'])
        author = self.request.user
        serializer.save(author=author, post=post)


class CommentListView(generics.ListAPIView):
    queryset = Commentary.objects.all()
    serializer_class = CommentarySerializer
    permission_classes = [permissions.IsAuthenticated, IsBuyerOrReadOnly]
