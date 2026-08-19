from django.urls import path
from blog.views import *
from django.views.generic.base import RedirectView

app_name = 'blog'

urlpatterns = [
    path("", IndexView.as_view(),name='index'),
    path("go_to_google/<int:pk>", RedirectView.as_view("https://google.com"), name="go_to_google")
]