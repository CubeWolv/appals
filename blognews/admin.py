from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug' ,'tags','status', 'created_on')
    search_fields = ('status', 'title', 'slug')

    def approve_comments(self, request, queryset):
        queryset.update(active=True)