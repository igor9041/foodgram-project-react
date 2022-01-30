from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

from .filters import RecipeFilter
from .models import Recipe, Tag, Ingredient
from users.models import CustomUser
from .serializers import RecipeSerializer, RecipeSerializerGet, TagSerializer, IngredientSerializer, M2MUserRecipeSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = None


class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    pagination_class = None


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.select_related('author').prefetch_related(
        'ingredients'
    ).all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        AllowAny,
    ]
    filterset_class = RecipeFilter

    def get_serializer_class(self):
        if self.request.method in permissions.SAFE_METHODS:
            return RecipeSerializerGet
        return RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def base_func(self, request, **kwargs):
        user = request.user
        recipe = get_object_or_404(Recipe, id=kwargs['id'])
        field_url = kwargs['field_url']
        if field_url == 'favorite':
            obj_exists = CustomUser.objects.filter(
                id=user.id,
                favourite_recipes=recipe
            ).exists()
            field = recipe.favorite_this
        elif field_url == 'shopping_cart':
            obj_exists = CustomUser.objects.filter(
                id=user.id,
                shopping_carts=recipe
            ).exists()
            field = recipe.shopping_cart
        if request.method == 'POST':
            field.add(user)
            serializer = M2MUserRecipeSerializer(recipe)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if request.method == 'DELETE' and obj_exists:
            recipe.favorite_this.remove(user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'detail': 'Действие уже выполнено'},
            status=status.HTTP_400_BAD_REQUEST
        )

    @action(
        detail=False,
        methods=['post', 'delete'],
        url_path=r'(?P<id>[\d]+)/favorite',
        url_name='favorite',
        pagination_class=None,
        permission_classes=[permissions.IsAuthenticated]
    )
    def favorite(self, request, **kwargs):
        return(self.base_func(request, **kwargs, field_url='favorite'))

    @action(
        detail=False,
        methods=['post', 'delete'],
        url_path=r'(?P<id>[\d]+)/shopping_cart',
        url_name='shopping_cart',
        pagination_class=None,
        permission_classes=[permissions.IsAuthenticated]
    )
    def shopping_cart(self, request, **kwargs):
        return(self.base_func(request, **kwargs, field_url='shopping_cart'))
