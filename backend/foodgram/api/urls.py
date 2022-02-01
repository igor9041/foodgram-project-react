from rest_framework.routers import DefaultRouter
from djoser import views
from django.urls import include, path


from .views import UserViewSet, TagViewSet, IngredientsViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('tags', TagViewSet, basename='tags')
router.register('ingredients', IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/token/login/', views.TokenCreateView.as_view(), name='login'),
    path('auth/token/logout/', views.TokenDestroyView.as_view(), name='logout')
]
