from django.urls import include, path
from ..views import * 

urlpatterns = [
    # profile user
    path('profile/', ProfileApiView.as_view(), name="profile")

]
