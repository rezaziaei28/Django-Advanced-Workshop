from django.urls import path
from blog.views import *
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path("", IndexView.as_view(),name='index'),
    path("go_to_jadi_dot_net/<int:pk>", RedirectToJadiDotNet.as_view(), name="go_to_jadi_dot_net"),
    path("post/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name='post-detail'),
    path("post/create/", PostCreateView.as_view(), name='post-create')
]