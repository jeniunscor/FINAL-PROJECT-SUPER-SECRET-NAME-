from django.contrib import admin


from apps.posts.models import (
    Category,
    Post,
    PostImage,
    Commentary,
)


@admin.register(Category)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(PostImage)
class WorkAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class WorkAdmin(admin.ModelAdmin):
    pass
