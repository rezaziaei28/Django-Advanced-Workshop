from django.urls import include, path

urlpatterns = [
      # accounts
      path('', include('accounts.api.v1.urls.accounts')),
      
      # profile user
      path('profile/', include('accounts.api.v1.urls.profile'))

]
