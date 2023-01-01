from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from blognews.models import Post
from django.contrib.auth.models import User
from taggit.models import Tag

 
 
def index(request, id, name):
    post = get_object_or_404(Post, id=id)
    data = Post.objects.get(id=id)
    user = User.objects.get(username='imran')
    recent_posts = Post.objects.exclude(id=id).order_by('-created_on')[:7]  # get the most recent 5 posts
    return render(request, './homepage/home.html', {"post": post,'recent_posts': recent_posts,'user':user})
