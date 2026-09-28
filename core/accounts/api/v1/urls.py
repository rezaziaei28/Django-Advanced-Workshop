from django.urls import include, path
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken

app_name = 'api_v1'

urlpatterns = [
    # registration
    path("register/", views.RegisterAPIView.as_view(), name="register"),

    # change password
    
    # reset password

    # login tocken
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),

    # logout
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),

    
    # login JWT  
]
