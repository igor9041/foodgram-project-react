from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from django.urls import include, path
from djoser import views

from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/login/', views.TokenCreateView.as_view(), name='login'),
    path('auth/token/logout/', views.TokenDestroyView.as_view(), name='logout')
]
