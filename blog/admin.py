from django.contrib import admin
from .models import Post


# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'datetime_created', 'status')
    ordering = ('id', )


admin.site.register(Post, PostAdmin)
