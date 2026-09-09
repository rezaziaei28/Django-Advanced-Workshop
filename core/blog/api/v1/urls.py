from django.urls import path
from .views import *


app_name = 'api-v1'

urlpatterns = [
    # This path is about function base view 
    # path("post/", post_list, name="post-list"),
    # path("post/<int:id>/", post_detail, name="post-detail")

    # This path is about class base view PostDetail 
    path("post/", PostList.as_view(), name="post-list"),
    path("post/<int:id>/", PostDetail.as_view(), name="post-detail")

]