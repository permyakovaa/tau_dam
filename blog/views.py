from django.shortcuts import render

# Create your views here.
from .models import Post


def blog_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, "blog/blog_list.html", context)


def blog_details(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }

    return render(request, "blog/blog_details.html", context)
