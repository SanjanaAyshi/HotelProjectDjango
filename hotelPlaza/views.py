from django.shortcuts import render
from post.models import Post


# def home(request):
#     data = Post.objects.all()
#     return render(request, 'home.html', {'data': data})

def home(request):
    data = Post.objects.all()
    return render(request, 'home.html', {'data': data})

def about_me(request):
    return render(request, 'about_us.html')