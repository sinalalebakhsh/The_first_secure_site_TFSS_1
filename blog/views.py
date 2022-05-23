from django.shortcuts import render
from .models import Post


def post_list_view(request):
    entire_posts = Post.objects.all()
    return render(request, 'blog/posts.html', {'posts_list': entire_posts})
