from django.urls import include, path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,  
    TokenVerifyView,
)

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
    path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),
]
