from django.contrib import admin


from apps.posts.models import (
    Category,
    Post,
    PostImage,
    Commentary,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Commentary)
class CommentaryAdmin(admin.ModelAdmin):
    pass
