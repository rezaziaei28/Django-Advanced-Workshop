from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostForm
# Create your views here.

# a function view for show a templates
"""
def function_name(request):
    '''
    a function base view for show index page
    '''
    context = {'post': Post}
    return render(request,'name_page.html',context)
"""

class IndexView(TemplateView):
    '''
    a class base view for show index page
    '''
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.all()
        return context
    

""" FBV for Redirect
from django.shortcuts import redirect
def redirect_to_google(request):
    '''
    This function redirect to desired site
    '''
    return redirect('https://google.com')
"""


class RedirectToJadiDotNet(RedirectView):
    '''
    Redirect view simple for google
    '''
    
    url = 'https://jadi.net/'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        return super().get_redirect_url(*args, **kwargs)


class PostListView(ListView):
    '''
    This class show all post on page
    '''

    # model = Post This is two solition for getting Post form models 
    # queryset = Post.objects.all()

    context_object_name = 'posts'
    paginate_by = 1 # for next page url/?page=2

    def get_queryset(self):
        posts = Post.objects.filter(status=1)
        return posts

class PostDetailView(DetailView):

    '''
    This class show a post on page
    '''
    model = Post

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

""" Learn FormView
class PostCreateView(FormView):
    '''
    This class create a new post with (FormView)
    '''
    template_name = "contact.html"
    form_class = PostForm
    success_url = "/blog/post/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""


class PostCreateView(CreateView):
    '''
    This class is create a new post with (CreateView) 
    '''

    model = Post
    # fields = ['author', 'title', 'content', 'category', 'status', 'published_date']
    form_class = PostForm
    success_url = '/blog/post/'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)
    

class PostEditView(UpdateView):
    '''
    This class is for edit a post 
    '''    

    model = Post
    form_class = PostForm
    success_url = '/blog/post/'
    
class PostDeleteView(DeleteView):
    '''
    This class is for delete post 
    '''

    model = Post
    success_url = '/blog/post/'

