from djoser.views import TokenCreateView
from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path(r'', include(router.urls)),
    path('auth/token/login/',
         TokenCreateView.as_view(),
         name='login'),
]