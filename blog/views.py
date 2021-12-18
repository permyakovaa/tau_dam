from django.shortcuts import render

# Create your views here.
from .models import Post, Project


def blog_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, "project/list.html", context)


def blog_details(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }

    return render(request, "project/details.html", context)


def projects_list(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, "project/list.html", context)
