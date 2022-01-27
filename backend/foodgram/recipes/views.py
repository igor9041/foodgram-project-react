from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .filters import IngredientNameFilter
from .serializers import TagSerializer, IngredientSerializer
from .models import Tag, Ingredient


class BaseViewSet(viewsets.ReadOnlyModelViewSet):
    pagination_class = None
    permission_classes = (AllowAny,)


class TagViewSet(BaseViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(BaseViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filterset_class = IngredientNameFilter
