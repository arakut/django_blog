from django.contrib import admin

# Register your models here.
from blog.models import Post




class PostAdmin(admin.ModelAdmin):
    list_display = ('image', 'title', 'desc')
    search_fields = ['title']

admin.site.register(Post, PostAdmin)