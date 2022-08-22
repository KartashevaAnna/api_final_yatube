from django.contrib import admin
from .models import Comment, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text')

admin.site.register(Post, PostAdmin)
