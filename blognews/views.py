from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from .models import Post
from django.utils.text import slugify
from .forms import AddPostForm
from django.db.models import  Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def blognews(request):
    user = User.objects.get(username='imran')
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

    
    return render(request, "./blogs/allblogs.html",{"posts": posts,'page_obj': posts, 'q':q ,'paginator': paginator,'user': user })







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

#allowing a specific user
def user_is_specific_user(user):
    return user.username == 'imran'


@user_passes_test(user_is_specific_user)
def addpost(request):
    if request.method == 'POST':
        # Bind the form to the request POST data
        form = AddPostForm(request.POST, request.FILES)

        # Check if the form is valid
        if form.is_valid():
          
            post = form.save(user=request.user)
            # Redirect to the post detail page
            return redirect('blognews')
    else:
        # Create an instance of the form
        form = AddPostForm()
    # Render the form template
    return render(request, './addpost/addpost.html', {'form': form})






login_required
@user_passes_test(user_is_specific_user)
def editpost(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = AddPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blognews')
    else:
        form = AddPostForm(instance=post)
    return render(request, './addpost/addpost.html', {'form': form})
