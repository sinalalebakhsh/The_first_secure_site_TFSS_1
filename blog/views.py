from django.shortcuts import render
from .models import Post
from django.http import HttpResponse


def post_list_view(request):
    entire_posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts_list': entire_posts})


def post_detail_view(request, pk):
    print('id in url: ', pk)
    return HttpResponse(f'id: {pk}')

