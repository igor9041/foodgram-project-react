from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, TagViewSet, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, 'users'),
router.register('tags', TagViewSet, 'tags'),
router.register('ingredients', IngredientViewSet, 'ingredients'),

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('djoser.urls.authtoken')),
]
