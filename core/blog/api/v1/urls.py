from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

app_name = 'api-v1'

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
urlpatterns = router.urls

# urlpatterns = [
#     # This path is about function base view 
#     # path("post/", post_list, name="post-list"),
#     # path("post/<int:id>/", post_detail, name="post-detail")

#     # This path is about class base view PostList and PostDetail 
#     # path("post/", PostList.as_view(), name="post-list"),
#     # path("post/<int:id>/", PostDetail.as_view(), name="post-detail")

#     # This path is about viewset
#     path('post/', PostViewSet.as_view({'get':'list','post':'create'}), name='post-list'),
#     path('post/<int:id>/', PostViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy', 'patch':'partial_update'}), name='post-retrieve'),

# ]