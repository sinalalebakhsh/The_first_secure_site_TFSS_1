from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def post_list_view(request):
    entire_posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', {'posts_list': entire_posts})


def post_detail_view(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        post = None
        print('Exception ObjectDoesNotExist')
    return render(request, 'blog/post_detail.html', {'post': post})

