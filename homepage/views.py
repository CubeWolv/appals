from django.http import HttpResponse
from taggit.managers import TaggableManager
from django.shortcuts import render,get_object_or_404
from blognews.models import Post
from taggit.models import Tag


 
def index(request, id, name):
    post = get_object_or_404(Post, id=id)
    data = Post.objects.get(id=id)
    tags = post.tags.all()
    related_posts = []
    for tag in tags:
        for tagged_item in tag.taggit_taggeditem_items.all()[:5]:
            related_posts.extend([tagged_item.content_object])
    # filter out the current post from the related posts list
    related_posts = [p for p in related_posts if p.id != id]
    return render(request, './homepage/home.html', {
        "post": post,
        'current_article': Post,
        'related_posts': related_posts
    })

