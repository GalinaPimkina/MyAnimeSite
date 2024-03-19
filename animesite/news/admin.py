from django.contrib import admin

from news.models import Post, PostTag, Category, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'action', 'post_slug']
    list_per_page = 15
    ordering = ['time_create', 'title', 'action']
    search_fields = ['title', 'action']
    filter_horizontal = ['category', 'tag']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'time_create', 'time_update']
    list_per_page = 15
    ordering = ['time_create', 'time_update']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_slug']
    list_per_page = 15
    ordering = ['name', 'category_slug']
    search_fields = ['name', 'category_slug']


@admin.register(PostTag)
class PostTagAdmin(admin.ModelAdmin):
    list_display = ['name', 'tag_slug']
    list_per_page = 15
    ordering = ['name', 'tag_slug']
    search_fields = ['name', 'tag_slug']