from django.db.models import Q
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from blog.models import Post


class ListObjectsView(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'


class DetailObjectsView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'


class SearchResultView(ListView):
    model = Post
    template_name = 'search_result.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(Q(title__icontains=query))
        return object_list

class NeedUpdateView(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = 'title','desc'
    success_url = '/'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'delete.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['image', 'title', 'desc', 'author']
    success_url = '/'
    template_name = 'create.html'