from django.urls import include, path
from .views import * 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,  
    TokenVerifyView,
)

app_name = 'api_v1'

urlpatterns = [
    # registration
    path("register/", RegisterAPIView.as_view(), name="register"),

    # change password
    path('password-change/', ChangePasswordApiView.as_view(), name='change-password'),

    # reset password

    # login tocken
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),

    # logout
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),
    
    # login JWT  
    # path('jwt/create/', TokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='jwt-verify'),

    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='jwt-create'),

    # profile user
    path('profile/', ProfileApiView.as_view(), name="profile")

]
