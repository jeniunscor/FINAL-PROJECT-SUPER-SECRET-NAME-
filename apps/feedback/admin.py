from django.contrib import admin

from apps.feedback.models import (
    Feedback,
)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass
