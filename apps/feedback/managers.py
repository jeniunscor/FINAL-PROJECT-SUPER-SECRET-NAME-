from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response


class FeedbackMessageManager:
    @staticmethod
    def perform_create(feedback_message, request_user):
        message = f"Имя пользователя: {feedback_message.name}\n" \
                  f"{feedback_message.message}\n\n" \
                  f"Контакт для обратной связи: {feedback_message.contact}"
        send_mail(
            f"Feedback from {request_user.email}",
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        return Response({"message": "Ваше сообщение успешно отправлено."})
