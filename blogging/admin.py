from django.contrib import admin
from django.db import models
from blogging.models import Post, Category


class CategoryInline(admin.StackedInline):
    model = Category.posts.through
    model.min_num = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)