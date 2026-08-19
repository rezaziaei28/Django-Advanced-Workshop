from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from blog.models import Post
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
    template_name = "TEMPLATE_NAME"

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


class redirect_to_google(RedirectView):
    '''
    Redirect view simple for google
    '''
    
    url = 'https://google.com'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pid'])
        return super().get_redirect_url(*args, **kwargs)
    