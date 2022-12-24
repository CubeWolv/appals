from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from django.utils.text import slugify
from django.http import Http404
from django.db.models import  Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blognews(request):
    posts = Post.objects.all()
    q=[]
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.filter( Q(title__icontains=q) |  Q(content__icontains=q) | Q(slug__icontains=q))
    paginator = Paginator(posts, 15) 
    page_number = request.GET.get('page')
    
    try:
        posts = paginator.get_page(page_number) 
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    
    return render(request, "./blogs/allblogs.html",{"posts": posts,'page_obj': posts, 'q':q ,'paginator': paginator })







def search(request):
    q=[]
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.filter( Q(title__icontains=q) | Q(content__icontains=q) | Q(slug__icontains=q))    

    elif 'all' in request.GET:
        all=request.GET['all']
        posts=Post.objects.filter(is_complete=True)


    else:
        posts=Post.objects.filter(is_complete=True)

        return render(request, "./blogs/allblogs.html",{"posts": posts ,"q":q})




def addpost(request):
    campID = 1
    if request.method == 'POST':
        # create a new Post instance with the provided data
        post = Post.objects.create(
            author=request.user,
            title=request.POST['title'],
            slug=request.POST['slug'],
            postimage =request.FILES['postimage'],
            content=request.POST['content'],
        )
        # get the tags string, split it into a list, and convert each tag to a slug
        tags = request.POST.get('tags').split(',')
        tags = [slugify(tag) for tag in tags]
        # set the tags field using the set method of the TaggableManager
        post.tags.set(tags)
        campID = post.id
        # save the Post instance to the database
        post.save()
        post
       
        return redirect('blognews')
    return render(request, './addpost/addpost.html')




def editpost(request, id):
    # retrieve the object to be edited
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        # handle the POST request by updating the object
        post.title=request.POST['title'],
        post.slug=request.POST['slug'],
        post.postimage=request.FILES['postimage']
        post.content=request.POST['content'],
        post.tags=request.POST['tags']

        # and so on for each field in the form
        post.save()
        return redirect('blognews')
    else:
        # render the template with the object's data
        return render(request, './addpost/editpost.html',{'post':post})

