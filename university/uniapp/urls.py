from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("applications/", ApplicationView.as_view(), name="application"),
    path("applications/<int:pk>/", StatusChangeView.as_view(), name="status_change"),
    path("users/", UserView.as_view(), name="users"),
    path("users/<int:pk>/", ClassroomAssignView.as_view(), name="user_classroom"),
]
