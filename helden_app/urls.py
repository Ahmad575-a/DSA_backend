from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HeldViewSet
from .views_auth import RegisterView, UserListView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'helden', HeldViewSet, basename='held')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/', obtain_auth_token, name='login'),
    path('users/', UserListView.as_view(), name='user-list'),
]

