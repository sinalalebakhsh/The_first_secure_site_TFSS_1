from django.shortcuts import render
from .models import Post
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


def post_list_view(request):
    # entire_posts = Post.objects.all()
    just_published = Post.objects.filter(status='pub')
    return render(request, 'blog/posts_list.html', {'posts_list': just_published})


def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'POST':
        print(request.POST.get('title'))
        print(request.POST.get('text'))
    else:
        print('Get request *********')
    return render(request, 'blog/post_create.html')

