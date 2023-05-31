from django.contrib import admin

from apps.feedback.models import (
    Feedback,
    Favorite,

)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    pass


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    pass
