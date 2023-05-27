from rest_framework import generics, permissions

from apps.feedback.serializers import FeedbackSerializer
from apps.feedback.managers import FeedbackMessageManager


class FeedbackMessageCreateView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        feedback_message = serializer.save(user=self.request.user)
        return FeedbackMessageManager.perform_create(
            feedback_message, self.request.user
        )
