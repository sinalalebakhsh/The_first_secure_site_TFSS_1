from django.shortcuts import render, redirect
from .models import Post
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views import generic
from .forms import NewPostForm


# def post_list_view(request):
#     # entire_posts = Post.objects.all()
#     just_published = Post.objects.filter(status='pub').order_by('-datetime_modified')
#     return render(request, 'blog/posts_list.html', {'posts_list': just_published})




def post_detail_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_create_view(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post list view')
    else:  # get request
        form = NewPostForm()
    return render(request, 'blog/post_create.html', context={'form': form})


def post_update_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = NewPostForm(request.POST or None, instance=post)

    if form.is_valid():
        form.save()
        return redirect('post list view')

    return render(request, 'blog/post_create.html', context={'form': form})


def post_delete_view(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('post list view')

    return render(request, 'blog/post_delete.html', context={'post': post})























