from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, IngredientsViewSet, RecipeViewSet


router = DefaultRouter()
router.register('tags', TagViewSet, basename='tags')
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register('ingredients', IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
]
