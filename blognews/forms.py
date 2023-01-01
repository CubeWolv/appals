from django import forms
from taggit.forms import TagField, TagWidget
from tinymce.widgets import TinyMCE
from .models import Post

class AddPostForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    slug= forms.CharField(max_length=255)
    postimage = forms.ImageField()
    content = forms.CharField(widget=TinyMCE())

    class Meta:
        model = Post
        fields = ['title','author','postimage','slug', 'content']
        widgets = {
            'content': TinyMCE(),
        }


    def save(self, commit=True, user=None):
        # Save the form data to the database
        instance = super().save(commit=False)
        if user:
            instance.author = user
        if commit:
            instance.save()
