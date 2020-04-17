from django.contrib import admin
from django.db import models
from django.forms import ModelForm
from blogging.models import Post, Category, Comment


class CategoryInline(admin.StackedInline):
    model = Category.posts.through


class PostAdmin(admin.ModelAdmin):
    list_filter = ['author', 'published_date']
    inlines = [CategoryInline]


class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'text', 'published_date']
    list_filter = ['author', 'published_date']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)