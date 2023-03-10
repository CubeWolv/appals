from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField 

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, blank=True)
    slug = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    postimage =  models.ImageField(upload_to='files/', default='/logo.png', null=True, blank=False)
    updated_on = models.DateTimeField(auto_now= True)
    content =   HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

    class Meta:
        ordering = ['-created_on']
        

    def __str__(self):
        return self.title
