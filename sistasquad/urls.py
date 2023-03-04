from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  path('signin', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
  path('signup', views.RegisterView.as_view(), name='auth_register'),

  path('profile', views.getProfile),
]