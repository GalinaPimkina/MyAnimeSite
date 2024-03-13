from django.contrib import admin

from news.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'action', 'post_slug']
    list_per_page = 15
    ordering = ['time_create', 'title', 'action']
    search_fields = ['title', 'action']
    filter_horizontal = ['category', 'tag']