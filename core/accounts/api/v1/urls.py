from django.urls import include, path
from . import views

app_name = 'api_v1'

urlpatterns = [
    # registration
    path("register/", views.RegisterAPIView.as_view(), name="register"),
    # change password
    
    # reset password

    # login tocken
    
    # login JWT  
]
