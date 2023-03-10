from django.contrib import admin
from .models import Category, Post, PostImage, Report


class ImageInline(admin.TabularInline):
    model = PostImage


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(PostImage)
admin.site.register(Report)
