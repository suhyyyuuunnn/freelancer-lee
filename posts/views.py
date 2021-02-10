from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.views.decorators.http import require_POST
from django.db.models import Q


def main(request):
    return render(request, 'posts/main.html')


def show(request):
    posts = Post.objects.order_by('-updated_at')
    post_sorted3 = []
    post_sorted2 = []
    post_sorted0 = []

    for post in posts:
        if post._type == 3:
            post_sorted3.append(post)
        elif post._type == 2:
            post_sorted2.append(post)
        elif post._type == 0:
            post_sorted0.append(post)

    context = {
        'posts': posts,
        'post_sorted3': post_sorted3,
        'post_sorted2': post_sorted2,
        'post_sorted0': post_sorted0,
    }
    return render(request, 'posts/show.html', context)


def service(request):
    return render(request, 'posts/service.html')


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.save()
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)


def search(request):
    posts = Post.objects.all().order_by('-id')

    q = request.POST.get('q', "")

    if q:
        posts = posts.filter(Q(title__icontains=q) | Q(content__icontains=q))
        return render(request, 'posts/search.html', {'posts': posts, 'q': q})
    else:
        return render(request, 'posts/show.html')